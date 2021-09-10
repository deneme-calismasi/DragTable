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


hello_button = Button(root, text="Hello", pady=6)

hello_button.pack()

label = Label(root, bg="red", width=8, height=4, text=time_func(), fg='blue', pady=10, padx=10, font=10)
label.place(x=150, y=150)
# label.config(text=print_func())

label2 = Label(root, bg="blue", width=8, height=4, text="BLUE")
label2.place(x=300, y=300)

label3 = Label(root, bg="green", width=8, height=4, text="GREEN")
label3.place(x=450, y=450)

rectangle1 = Canvas(root, width=500, height=200)
rectangle1.pack()

rectangle1.create_rectangle(20, 140, 120, 180, fill="red")
rectangle1.create_text(70, 130, text="Projects--20%")
rectangle1.create_rectangle(140, 160, 240, 180, fill="blue")
rectangle1.create_text(190, 150, text="Quizzes--10%")
rectangle1.create_rectangle(260, 120, 360, 180, fill="green")
rectangle1.create_text(310, 110, text="Midterm--30%")
rectangle1.create_rectangle(380, 100, 480, 180, fill="orange")
rectangle1.create_text(430, 90, text="Final--40%")
rectangle1.create_line(0, 180, 500, 180)

rect2 = Canvas(root, width=250, height=250)
rect2.pack()
rect2.create_rectangle(40, 180, 160, 220, fill="black")
rect2.create_text(70, 130, text=time_func())

rectangle1.bind("<Button-1>", drag_start)
rectangle1.bind("<B1-Motion>", drag_motion)

rect2.bind("<Button-1>", drag_start)
rect2.bind("<B1-Motion>", drag_motion)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

label3.bind("<Button-1>", drag_start)
label3.bind("<B1-Motion>", drag_motion)

hello_button.bind("<Button-1>", drag_start)
hello_button.bind("<B1-Motion>", drag_motion)

get_mongo()
root.mainloop()
