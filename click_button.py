from tkinter import *
from tkinter import ttk
import tkinter.messagebox


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
        button1.bind("<Button-1>", self.drag_start)
        button1.bind("<B1-Motion>", self.drag_motion)

        self.label = Label(self.txt_frm, text='')
        self.label.grid(column=1, row=3)
        self.label.bind("<Button-1>", self.drag_start)
        self.label.bind("<B1-Motion>", self.drag_motion)

    def hello_world(self):
        self.label.config(text="HELLO WORLD!")

    def drag_start(self, event):
        widget = event.widget
        widget.startX = event.x
        widget.startY = event.y

    def drag_motion(self, event):
        widget = event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x, y=y)

    def fire_here(self, x, y):
        print("column:{}, row:{}".format(x, y))


status = Label(root, text="Preparing to begin...", bd=1, relief=SUNKEN,
               anchor=W)  # bd = bordered, relief = ,  appear placed in screen, anchor = w (NESW) needs two other properties
status.pack(side=BOTTOM, fill=X)
app = App(root)
root.mainloop()
