import tkinter as tk
import random

root = tk.Tk()


def update_btn_text():
    x = random.randint(10000, 100000)
    btn_text.set(x)
    do_popup()


def do_popup():
    x, y = btn.winfo_rootx(), btn.winfo_rooty()
    print(x, y)


btn_text = tk.StringVar()
btn = tk.Button(root, textvariable=btn_text, command=update_btn_text)

btn_text.set("a")

# btn.pack()
btn.place(x=250, y=77)

root.mainloop()
