import datetime as dt
from tkinter import *
import numpy as np
import pandas as pd
import pymongo
import random
from functools import partial


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
    x = button[i].winfo_rootx()
    print("x= ", x)
    return x


def do_popup_y():
    y = button[i].winfo_rooty()
    print("y= ", y)
    return y


def label_place():
    label[i].place(x=(do_popup_x() + 10), y=(do_popup_y() - 65))


def random_func():
    txt = random.randint(0, 100)
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

str1 = ''.join(sensor_no)

new_lst_1 = list(str(str1))

new_lst_2 = list(map(int, new_lst_1))
print(new_lst_2)

button = []
label = []


def callback_function(func_var):
    label_place()
    print('Pressed:', func_var)


for i in range(len(new_lst_2)):

    for index, dat, in enumerate(sensor_no):
        button.append(Button(root, text=dat, bg="red", fg="white", command=lambda dat=dat: callback_function(dat)))
        button[i].pack()

        label.append(Label(root, text=random_func(), bg="black", fg="blue"))
        label[i].pack()

        button[i].bind("<Button-1>", drag_start)
        button[i].bind("<B1-Motion>", drag_motion)
        label[i].bind("<Button-1>", drag_start)
        label[i].bind("<B1-Motion>", drag_motion)
        print(button[i])

root.mainloop()
