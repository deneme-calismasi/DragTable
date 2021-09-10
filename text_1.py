import tkinter.messagebox
from tkinter import *


def new():
    tkinter.messagebox.showinfo('Window Title', 'Well, this is new...')


root = Tk()
root.title("GUI Test Version 2")
root.resizable(False, False)
root.geometry('{}x{}'.format(400, 400))
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Experiment...", command=new)
subMenu.add_command(label="New...", command=new)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.destroy)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=new)
toolbar = Frame(root, bg="light blue")
toolbar.pack(side=TOP, fill=X)


class App(object):
    def __init__(self, root):
        self.root = root

        self.txt_frm = Frame(self.root, width=900, height=900)
        self.txt_frm.pack(fill="both", expand=True)

        button1 = Button(self.txt_frm, text="HELLO", command=self.hello_world)
        button1.grid(column=0, row=2, padx=2, pady=2)

        self.label = Label(self.txt_frm, text='')
        self.label.grid(column=5, row=5)

    def hello_world(self):
        self.label.config(text="HELLO WORLD!")


app = App(root)
root.mainloop()
