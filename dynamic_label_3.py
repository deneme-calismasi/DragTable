from tkinter import *
import tkinter.ttk as ttk

master = Tk()
data2 = ['Orange', 'Apple', 'Banana', 'Kiwi']
button_dict = {}


def callback_function(x): print('Pressed:', x)


for index, dat in enumerate(data2):
    button = ttk.Button(master, text=dat[0],
                        command=lambda dat=dat: callback_function(dat))
    button.grid(row=index + 1, column=1, pady=0, padx=0)
    button_dict[dat] = button  # Stores a reference to the button under
    # the name from the database

for name in data2:
    print(name, button_dict[name])  # prints all button/name associations

master.mainloop()
