import tkinter as tk
import random

root = tk.Tk()


def update_btn_text():
    x = random.randint(0, 100)
    btn_text.set(x)


btn_text = tk.StringVar()
btn = tk.Button(root, textvariable=btn_text, command=update_btn_text)
btn_text.set("a")

btn.pack()

root.mainloop()
