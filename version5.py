import datetime as dt
from tkinter import *

import pymongo


def get_mongo():
    global get_data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sensor_Record"]
    mycol = mydb["data1"]
    for get_data in mycol.find({}, {"_id": 0, "Sensor No": 1}):
        print(get_data)
    return get_data


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

# root.configure(bg='white')


hello_button = Button(root, text=get_mongo(), pady=6)

hello_button.pack()

hello_button.bind("<Button-1>", drag_start)
hello_button.bind("<B1-Motion>", drag_motion)

get_mongo()
root.mainloop()
