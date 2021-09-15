import tkinter as tk
import random

root = tk.Tk()
root.title("DragTable")
root.geometry("800x600")
root.state('zoomed')


def update_btn_text():
    x = random.randint(10000, 100000)
    btn_text.set(x)
    do_popup_x()
    do_popup_y()


def do_popup_x():
    x = btn.winfo_rootx()
    print("x= ", x)
    return x


def do_popup_y():
    y = btn.winfo_rooty()
    print("y= ", y)
    return y


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
btn.place(x=btn.winfo_rootx(), y=btn.winfo_rooty())

root.mainloop()
