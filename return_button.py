import tkinter as tk


def do_popup():
    x, y = btn1.winfo_rootx(), btn1.winfo_rooty()
    print(x, y)


root = tk.Tk()
btn1 = tk.Button(root, text="POPUP", command=do_popup)
btn1.grid(row=100, column=100)
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="a")
menu.add_command(label="b")
menu.add_command(label="c")

root.mainloop()
