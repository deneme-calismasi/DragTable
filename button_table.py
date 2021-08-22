import tkinter as tk
from tkinter import ttk


class ButtonTree(ttk.Frame):
    def __init__(self, parent, items):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.items = items
        self.tree = MyTree(self, items)
        self.tree.grid(column=0, row=0, sticky=tk.N)
        self.buttons = ttk.Frame(self, width=100)
        self.buttons.grid(column=1, row=0, sticky=tk.N)
        print(self.tree.config())

    def create_buttons(self):
        self.update()
        so_far = header_height = 16 + 2
        ttk.Frame(self.buttons).place(in_=self.buttons, x=0, y=0, width=100, height=header_height)

        for item_name, item in zip(self.tree.get_children(), self.items):
            print(item_name, item, self.tree.bbox(item_name))
            button = ttk.Button(self.buttons, text="Do Something...")
            h = self.tree.bbox(item_name)[-1]
            button.place(in_=self.buttons, x=0, y=so_far, width=100, height=h)
            so_far += h

        self.buttons["height"] = len(self.items) * 20 + header_height


class MyTree(ttk.Treeview):
    def __init__(self, parent, items):
        ttk.Treeview.__init__(self, parent, columns=("A"), padding=1)
        self.heading("A", text="Some A")
        self.parent = parent
        self.items = items
        for item in self.items:
            self.insert(parent="", index="end", text=item, values="hello")


if __name__ == "__main__":
    root = tk.Tk()
    buttonTree = ButtonTree(root, list(range(10)))
    buttonTree.pack()
    buttonTree.create_buttons()
    root.mainloop()
