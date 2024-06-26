from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from scrollbar import ScrollFrame
from files import get_forms
from pdfs import get_fields, write_fields
import field_names
from input_gui import askRename

class MainWindow(Tk):
   def __init__(self, parent):
      Tk.__init__(self, parent)
      self.parent = parent
      self.selection = []
      self.fieldData = {}
      self.initialize()
      
   def initialize(self):
      # GUI
      self.grid()
      self.configure(padx=10, pady=10)
      # 5 Columns
      for i in range(5):
         self.grid_columnconfigure(i, weight=1)
      # 2 Rows, but only the first should be expandable
      self.grid_rowconfigure(0, weight=1)
      # self.grid_rowconfigure(1, weight=0)

      self.pdfList = ttk.Treeview(self, columns=('path'))
      self.pdfList.config(show='tree')
      #pdfList.column('path', width=1)
      # Insert items
      for listItem in get_forms():
         self.pdfList.insert(listItem['parent'], 'end', listItem['id'], text=listItem['name'])

      self.pdfList.grid(column=0, row=0, rowspan=1, columnspan=2, sticky='NSEW')

      # A button under the tree view to add custom pdfs
      # ttk.Button(frm, text='Add PDF', command=self.add_pdf).grid(column=0, row=1)
      ttk.Button(self, text='Map Fields', command=self.map_fields).grid(column=0, row=1, rowspan=2)
      ttk.Button(self, text='Load PDFs', command=self.get_selection).grid(column=1, row=1, rowspan=2)

      # Set up a frame in a canvas so a scrollbar can be added
      fieldsFrm = ttk.Frame(self, borderwidth=1, relief='sunken')
      fieldsFrm.grid(column=2, row=0, columnspan=3, sticky='NSEW')
      self.scrollFrame = ScrollFrame(fieldsFrm)
      # Make the canvas background the same color as frames
      s = ttk.Style()
      bg = s.lookup('TFrame', 'background')
      self.scrollFrame.viewPort.configure(background=bg)
      self.scrollFrame.pack(fill='both', expand=True)

      # Add controls under the data entry area
      self.outputLocation = StringVar()
      ttk.Label(self, text='Output Subfolder:').grid(column=2, row=1)
      ttk.Entry(self, textvariable=self.outputLocation).grid(column=2, row=2)
      ttk.Button(self, text="Save", command=self.save_pdfs).grid(column=3, row=1, rowspan=2)
      ttk.Button(self, text="Quit", command=self.quit).grid(column=4, row=1, rowspan=2)

   def map_fields(self):
      selection = self.pdfList.selection()
      for pdf in selection:
         fields = get_fields(pdf)
         # Copy field id as a value for that field
         fieldData = {fieldId: fieldId for fieldId in fields}
         write_fields(selection, fieldData, folder='FieldMapping')
         messagebox.showinfo('Saved', "Field names written to output/FieldMapping")

   def get_selection(self):
      ignoreList = field_names.get_ignore()
      renameDict = field_names.get_rename()
      print(renameDict)
      # Clear the old selection, if there is any
      self.fieldData = {}
      for child in self.scrollFrame.viewPort.winfo_children():
         child.destroy()
         
      # Get the selection and add fields
      self.selection = self.pdfList.selection()
      for pdf in self.selection:
         fields = get_fields(pdf)
         for fieldKey in fields:
            # If we're ignoring the field, ignore it
            if fieldKey in ignoreList:
               continue
            # Check for an alternate name in the rename dict
            ttString = renameDict[fieldKey] if fieldKey in renameDict else fieldKey
            # Create data in the fieldData dict if it doesn't already exist
            if ttString not in self.fieldData:
               # Create an initial data object. Leave out the field id here because it's added in both cases later
               self.fieldData[ttString] = {
                  "ids": [],
                  "data": StringVar()
               }
               # New fields also only need to be added if this field hasn't been seen yet
               row = len(self.fieldData) - 1
               ttk.Button(self.scrollFrame.viewPort, text='Hide', command=self.setup_ignore(fieldKey, row))\
                  .grid(column=0, row=row, pady=2)
               ttk.Button(self.scrollFrame.viewPort, text='Rename', command=self.setup_rename(fieldKey, row))\
                  .grid(column=1, row=row, pady=2)
               ttk.Label(self.scrollFrame.viewPort, text=ttString).grid(column=2, row=row, pady=2)
               ttk.Entry(self.scrollFrame.viewPort, textvariable=self.fieldData[ttString]['data'])\
                  .grid(column=3, row=row, pady=2)
            # Add the current field to the id array of the appropriate data field
            self.fieldData[ttString]['ids'].append(fieldKey)

   def setup_ignore(self, fieldId, row):
      _id = fieldId
      _r = row
      return lambda: self.add_ignore(_id, _r)

   def add_ignore(self, fieldId, row):
      if messagebox.askyesno('Hide Field', f'Hide Field: `{fieldId}` ?'):
         field_names.add_ignore(fieldId)
         items = self.scrollFrame.viewPort.grid_slaves(row=row)
         for i in items:
            i.grid_forget()

   def setup_rename(self, fieldId, row):
      _id = fieldId
      _r = row
      return lambda: self.rename_field(_id, _r)

   def rename_field(self, fieldId, row):
      result = askRename(fieldId)
      if result is not None:
         field_names.add_rename(fieldId, result)
         # Rename the existing displayed field
         for item in self.scrollFrame.viewPort.grid_slaves(row=row, column=2):
            item.grid_forget()
         ttk.Label(self.scrollFrame.viewPort, text=result).grid(column=2, row=row, pady=2)

   def add_pdf(self):
      messagebox.showinfo(message='Not Implemented')

   def save_pdfs(self):
      # Convert StringVars to actual strings
      data = {}
      for ttString in self.fieldData:
         # Multiple field ids could be associated with this string. The list is stored as 'ids'
         for fieldName in self.fieldData[ttString]['ids']:
            # Convert the StringVar to a real string
            data[fieldName] = self.fieldData[ttString]['data'].get()
      write_fields(self.selection, data, folder=self.outputLocation.get())
      messagebox.showinfo('Saved', "PDFs saved to output/" + self.outputLocation.get())

   def quit(self):
      self.destroy()
      field_names.save()

if __name__ == '__main__':
   app = MainWindow(None)
   app.title('Fill PDF')
   app.mainloop()