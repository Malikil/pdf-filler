from tkinter import *
from tkinter import ttk
import field_names

def input_window(field):
    pass

class InputWindow(Tk):
    def __init__(self, parent):
        Tk.__init__(self, parent)

        self.transient(parent)
        self.initialize()
        self.grab_set()

    def initialize(self):
        self.grid()
        self.config(padx=10, pady=10)

        self.renameFrom = StringVar()
        self.renameTo = StringVar()
        ttk.Label(self, text='Rename:').grid(row=0, column=0)
        ttk.Label(self, textvariable=self.renameFrom).grid(row=0, column=1)
        ttk.Label(self, text='To:').grid(row=1, column=0)
        ttk.Entry(self, textvariable=self.renameTo).grid(row=1, column=1)
        ttk.Button(self, text='Rename', command=self.rename).grid(row=3, column=0)
        ttk.Button(self, text='Cancel', command=self.done).grid(row=3, column=1)

    def rename(self):
        print(self.renameTo.get())
        self.done()

    def done(self):
        self.destroy()
