import datetime as dt
import tkinter.ttk as ttk
from tkinter import *

"""def get_mongo():
    global get_data
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Sensor_Record"]
    mycol = mydb["data1"]
    list_data = list(mycol.collection.find())
    # for get_data in mycol.find({}, {"_id": 0, "Sensor No": 1}):
    #     print(get_data)
    # list_data = list(get_data.keys())
    # print(list_data)
    print(list_data)
    return list_data"""


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


# hello_button = Button(root, text="text", pady=6)
#
# hello_button.pack()
#
# hello_button.bind("<Button-1>", drag_start)
# hello_button.bind("<B1-Motion>", drag_motion)

data2 = {'Orange': 5, 'Apple': 6, 'Banana': 7, 'Kiwi': 8, 'Corn': 9, 'Tomato': 10}
button_dict = {}


def callback_function(x): print('Pressed:', x)


for index, dat in enumerate(data2):
    button = ttk.Button(root, text=dat,
                        command=lambda dat=dat: callback_function(dat))
    button.grid(row=index + 1, column=1, pady=0, padx=0)
    button_dict[dat] = button  # Stores a reference to the button under
    # the name from the database
    button.bind("<Button-1>", drag_start)
    button.bind("<B1-Motion>", drag_motion)

for name in data2:
    print(name, button_dict[name])  # prints all button/name associations


# get_mongo()
root.mainloop()
