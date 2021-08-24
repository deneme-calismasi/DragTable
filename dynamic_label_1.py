import tkinter as tk

root = tk.Tk()

data = tk.StringVar()
data.set("This")


def change():
    if data.get() == "This":
        data.set("That")
    else:
        data.set("This")


tk.Label(root, textvariable=data).pack()
tk.Button(root, text="Change", command=change).pack()

root.mainloop()
