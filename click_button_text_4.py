from tkinter import *


def write_hello():
    w = Label(root, text="Hello. This is a label.")
    w.pack()


root = Tk()

button = Button(root, text="Hello!", command=write_hello)
button.pack()

root.mainloop()
