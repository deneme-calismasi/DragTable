import tkinter as tk
import random

root = tk.Tk()
root.title("DragTable")
root.geometry("800x600")
root.state('zoomed')


def update_btn_text():
    x = random.randint(10000, 100000)
    btn_text.set(x)
    do_popup()


def do_popup():
    x, y = btn.winfo_rootx(), btn.winfo_rooty()
    print(x, y)


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


btn_text = tk.StringVar()
btn = tk.Button(root, textvariable=btn_text, command=update_btn_text)

btn.bind("<Button-1>", drag_start)
btn.bind("<B1-Motion>", drag_motion)

btn_text.set("a")

# btn.pack()
btn.place(x=250, y=77)

root.mainloop()
