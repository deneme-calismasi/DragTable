import tkinter as tk


def check_pos(event):
    print(my_text.index(tk.INSERT))


root = tk.Tk()

my_text = tk.Text(root)
my_text.pack()
my_text.bindtags(('Text', 'post-class-bindings', '.', 'all'))

my_text.bind_class("post-class-bindings", "<KeyPress>", check_pos)
my_text.bind_class("post-class-bindings", "<Button-1>", check_pos)

root.mainloop()
