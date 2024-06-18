from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import Dialog
import field_names

def askRename(field):
    r = InputWindow(title='Rename', oldName=field)
    return r.result

class InputWindow(Dialog):
    def __init__(self, parent=None, title=None, oldName=''):
        # Define before calling the parent init because the custom body expects them
        self.renameFrom = StringVar(value=oldName)
        self.renameTo = StringVar()
        self.fieldList = field_names.get_rename().values()
        print(self.fieldList)

        Dialog.__init__(self, parent, title=title)

        # If the parent is not viewable, don't make the child transient,
        # or else it would be opened withdrawn
        # Whatever that means
        # if parent is not None and parent.winfo_viewable():
        #     self.transient(parent)
        
        # self.parent = parent
        # self.result = None
        # self.initialize()

        # self.protocol('WM_DELETE_WINDOW', self.done)
        # self.wait_visibility()
        # self.grab_set()
        # self.wait_window(self)

    # Override to create the dialog body
    def body(self, master):
        master.grid()
        master.config(padx=10, pady=10)
        
        ttk.Label(master, text='Rename:').grid(row=0, column=0)
        ttk.Label(master, textvariable=self.renameFrom).grid(row=0, column=1)
        ttk.Label(master, text='To:').grid(row=1, column=0)
        ttk.Entry(master, textvariable=self.renameTo).grid(row=1, column=1)
        # ttk.Button(master, text='Rename', command=self.rename).grid(row=3, column=0)
        # ttk.Button(master, text='Cancel', command=self.done).grid(row=3, column=1)

    # Override - Validate data before dialog is destroyed. Return bool
    def validate(self):
        return 1

    # Override - Process data after dialog is destroyed. No return value
    # To return the result, store in self.result
    def apply(self):
        self.result = self.renameTo.get()
