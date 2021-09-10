from tkinter import *
from tkinter import ttk

root = Tk()
board_frame = ttk.Frame(root, padding=5)
board_frame.grid(column=0, row=0)

COORDS_LIST = []
buttons_dict = {}


def fire_here(x, y):
    print("column:{}, row:{}".format(x, y))


for r in range(1, 11):
    for c in range(1, 11):
        coord = str(r) + "_" + str(c)
        COORDS_LIST.append(coord)

        buttons_dict[COORDS_LIST[-1]] = ttk.Button(board_frame, text="O", width="2")

        buttons_dict[COORDS_LIST[-1]]["command"] = lambda x=c, y=r: fire_here(x, y)

        buttons_dict[COORDS_LIST[-1]].grid(row=r, column=c)

root.mainloop()
