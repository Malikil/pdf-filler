from tkinter import *
from tkinter import ttk, messagebox
from scrollbar import ScrollFrame
from files import get_forms
from pdfs import get_fields, write_fields

class MainWindow:
   def __init__(self):
      self.selection = []
      self.fieldData = {}

      # GUI
      self.root = Tk()
      self.root.wm_title("Fill PDF")
      frm = ttk.Frame(self.root, padding=10)
      frm.grid()

      self.pdfList = ttk.Treeview(frm, columns=('path'))
      self.pdfList.config(show='tree')
      #pdfList.column('path', width=1)
      # Insert items
      for listItem in get_forms():
         self.pdfList.insert(listItem['parent'], 'end', listItem['id'], text=listItem['name'])

      self.pdfList.grid(column=0, row=0, rowspan=1, columnspan=2)

      # A button under the tree view to add custom pdfs
      # ttk.Button(frm, text='Add PDF', command=self.add_pdf).grid(column=0, row=1)
      ttk.Button(frm, text='Load PDFs', command=self.get_selection).grid(column=1, row=1)

      # Set up a frame in a canvas so a scrollbar can be added
      fieldsFrm = ttk.Frame(frm, borderwidth=1, relief='sunken')
      fieldsFrm.grid(column=2, row=0, columnspan=2)
      self.scrollFrame = ScrollFrame(fieldsFrm)
      # Make the canvas background the same color as frames
      s = ttk.Style()
      bg = s.lookup('TFrame', 'background')
      self.scrollFrame.viewPort.configure(background=bg)
      self.scrollFrame.pack()

      ttk.Button(frm, text="Save", command=self.save_pdfs).grid(column=2, row=1)
      ttk.Button(frm, text="Quit", command=self.root.destroy).grid(column=3, row=1)

   def get_selection(self):
      # Clear the old selection, if there is any
      self.fieldData = {}
      for child in self.scrollFrame.viewPort.winfo_children():
         child.destroy()
         
      fieldCount = 0
      # Get the selection and add fields
      self.selection = self.pdfList.selection()
      for i, pdf in enumerate(self.selection):
         fields = get_fields(pdf, i)
         fieldCount += len(fields)
         for field in fields:
            # Use the tooltip string as the primary key
            # Get tooltip string
            ttString = (fields[field]['/TU'] if '/TU' in fields[field] else field).lower()
            # Create data in the fieldData dict if it doesn't already exist
            if ttString not in self.fieldData:
               # Create an initial data object. Leave out the field id here because it's added in both cases later
               self.fieldData[ttString] = {
                  "ids": [],
                  "data": StringVar()
               }
               # New fields also only need to be added if this field hasn't been seen yet
               row = len(self.fieldData) - 1
               ttk.Label(self.scrollFrame.viewPort, text=ttString).grid(column=0, row=row, pady=2)
               ttk.Entry(self.scrollFrame.viewPort, textvariable=self.fieldData[ttString]['data']).grid(column=1, row=row, pady=2)
            # Add the current field to the id array of the appropriate data field
            self.fieldData[ttString]['ids'].append(field)
      print(fieldCount)
      print(len(self.fieldData))

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
      write_fields(self.selection, data)
      messagebox.showinfo('Saved', "PDFs Saved to 'output' folder")

   def mainloop(self):
      self.root.mainloop()

MainWindow().mainloop()