import datetime as dt
import tkinter.ttk as ttk
from tkinter import *

import numpy as np
import pandas as pd
import pymongo


def get_mongo():
    global get_data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sensor_Record"]
    mycol = mydb["data1"]

    documents = list(mycol.find({}, {'_id': 0}))

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


def callback_function(x): print('Pressed:', x)


for index, dat in enumerate(sensor_no):
    button = ttk.Button(root, text='Sensor ' + dat,
                        command=lambda dat=dat: callback_function(dat))
    button.grid(row=index + 1, column=1, pady=0, padx=0)
    button_dict[dat] = button  # Stores a reference to the button under
    # the name from the database
    button.bind("<Button-1>", drag_start)
    button.bind("<B1-Motion>", drag_motion)

for name in sensor_no:
    print(name, button_dict[name])  # prints all button/name associations

# get_mongo()
root.mainloop()
