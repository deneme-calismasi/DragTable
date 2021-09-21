import datetime as dt
import tkinter as tk
from tkinter import *
import numpy as np
import pandas as pd
import pymongo
import random

root = Tk()
root.geometry("800x600")
root.state('zoomed')


def get_mongo():
    global get_data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sensor_Record"]
    mycol = mydb["data1"]

    documents = list(mycol.find({"Sensor No": {'$gte': "1"}}, {'_id': 0}))

    print(documents)
    return documents


def random_func():
    txt = random.randint(0, 100)
    return txt


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


def do_popup_x():
    x = button[i].winfo_rootx()
    print("x= ", x)
    return x


def do_popup_y():
    y = button[i].winfo_rooty()
    print("y= ", y)
    return y


def button_place():
    label = Label(root, text=random_func(), bg="black", fg="blue")
    label.grid(row=do_popup_x(), column=do_popup_y(), pady=1, padx=1)
    label.place(x=(do_popup_x() + 10), y=(do_popup_y() - 65))


def time_func():
    time_data = dt.datetime.now().strftime('%Y-%m-%d %X')
    return time_data


def callback_function(func_var):
    button_place()
    print('Pressed:', func_var)


data2 = get_mongo()

df = pd.DataFrame.from_records(data2)

sensor_no = np.array(df['Sensor No'])

# print(sensor_no)

str1 = ''.join(sensor_no)

new_lst_1 = list(str(str1))

# print(list(str(str1)))

new_lst_2 = list(map(int, new_lst_1))
print(new_lst_2)

# print(new_lst)
# for _position, _value in enumerate(sensor_no):
#     try:
#         _new_value = float(_value)
#     except ValueError:
#         _new_value = 0.0
#     sensor_no[_position] = _new_value


files = []  # creates list to replace your actual inputs for troubleshooting purposes
button = []  # creates list to store the buttons ins
button_dict = {}

for i in range(
        len(new_lst_2)):  # this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
    files.append("Button " + str(i + 1))

    for index, dat, in enumerate(sensor_no):
        button[i].append(
            tk.Button(root, text=dat, bg="red", fg="white", command=lambda dat=dat: callback_function(dat)))
        # button[i].pack()  # this packs the buttons
        button[i].pack()
        button_dict[dat] = button[i]  # Stores a reference to the button under
        # the name from the database

        # label_dict[dat] = label
        button[i].bind("<Button-1>", drag_start)
        button[i].bind("<B1-Motion>", drag_motion)
        print(button[i])

root.mainloop()
