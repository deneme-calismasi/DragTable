import datetime as dt
import tkinter as tk
from tkinter import *
import numpy as np
import pandas as pd
import pymongo
import random


def get_mongo():
    global get_data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sensor_Record"]
    mycol = mydb["data1"]

    documents = list(mycol.find({"Sensor No": {'$gte': "1"}}, {'_id': 0}))

    print(documents)
    return documents


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
    x = button.winfo_rootx()
    print("x= ", x)
    return x


def do_popup_y():
    y = button.winfo_rooty()
    print("y= ", y)
    return y


def update_btn_text():
    txt = random.randint(0, 100)
    label.place(x=(do_popup_x() + 10), y=(do_popup_y() - 65))
    return txt


def time_func():
    time_data = dt.datetime.now().strftime('%Y-%m-%d %X')
    return time_data


root = Tk()
root.title("DragTable")
root.geometry("800x600")
root.state('zoomed')

data2 = get_mongo()
df = pd.DataFrame.from_records(data2)

sensor_no = np.array(df['Sensor No'])
button_dict = {}
label_dict = {}


def callback_function(func_var):
    update_btn_text()
    print('Pressed:', func_var)


for index, dat in enumerate(sensor_no):
    button = Button(root, text=dat, bg="red", fg="white", command=lambda dat=dat: callback_function(dat))
    button.grid(row=index + 1, column=1, pady=0, padx=0)
    button_dict[dat] = button  # Stores a reference to the button under
    # the name from the database
    label = Label(root, text="dat", bg="black", fg="blue")
    label.grid(row=do_popup_x, column=do_popup_y, pady=1, padx=1)
    label_dict[dat] = label
    button.bind("<Button-1>", drag_start)
    button.bind("<B1-Motion>", drag_motion)
    label.bind("<Button-1>", drag_start)
    label.bind("<B1-Motion>", drag_motion)

for name in sensor_no:
    print(name, button_dict[name])  # prints all button/name associations
    print(name, label_dict[name])

# get_mongo()
root.mainloop()
