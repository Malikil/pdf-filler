from tkinter import *
from tkinter import ttk
import field_names

class InputWindow(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)
        self.parent = parent
        self.selection = []
        self.fieldData = {}
        self.initialize()

    def initialize(self):
        self.grid()
        self.config(padx=10, pady=10)

        self.renameFrom = StringVar()
        self.renameTo = StringVar()
        ttk.Label(self, text='Rename:').grid(row=0, column=0)
        ttk.Label(self, textvariable=self.renameFrom).grid(row=0, column=1)
        ttk.Label(self, text='To:').grid(row=1, column=0)
        ttk.Entry(self, textvariable=self.renameTo).grid(row=1, column=1)
        ttk.Button(self, text='Rename').grid(row=3, column=0)
        ttk.Button(self, text='Cancel').grid(row=3, column=1)

class Mbox(object):

    root = None

    def __init__(self, msg, dict_key=None):
        """
        msg = <str> the message to be displayed
        dict_key = <sequence> (dictionary, key) to associate with user input
        (providing a sequence for dict_key creates an entry for user input)
        """
        self.top = Toplevel(Mbox.root)

        frm = ttk.Frame(self.top, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)

        label = ttk.Label(frm, text=msg)
        label.pack(padx=4, pady=4)

        caller_wants_an_entry = dict_key is not None

        if caller_wants_an_entry:
            self.entry = ttk.Entry(frm)
            self.entry.pack(pady=4)

            b_submit = ttk.Button(frm, text='Submit')
            b_submit['command'] = lambda: self.entry_to_dict(dict_key)
            b_submit.pack()

        b_cancel = ttk.Button(frm, text='Cancel')
        b_cancel['command'] = self.top.destroy
        b_cancel.pack(padx=4, pady=4)

    def entry_to_dict(self, dict_key):
        data = self.entry.get()
        if data:
            d, key = dict_key
            d[key] = data
            self.top.destroy()