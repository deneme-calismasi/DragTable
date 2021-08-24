import tkinter as tk

root = tk.Tk()

data = "This"


def change():
    global data
    if data == "This":
        data = "That"
        a_label['text'] = data
    else:
        data = "This"
        a_label.config(text=data)


a_label = tk.Label(root, text=data)
a_label.pack()
tk.Button(root, text="Change", command=change).pack()

root.mainloop()
