from tkinter import *


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


root = Tk()
root.title("DragTable")
root.geometry("540x480")
root.state('zoomed')
# root.configure(bg='white')

label = Label(root, bg="red", width=5, height=3, text="RED", fg='blue', pady=10, padx=10, font=10)
label.place(x=0, y=0)

label2 = Label(root, bg="blue", width=5, height=3, text="BLUE")
label2.place(x=100, y=100)

label3 = Label(root, bg="green", width=5, height=3, text="GREEN")
label3.place(x=200, y=200)

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

rectangle1.bind("<Button-1>", drag_start)
rectangle1.bind("<B1-Motion>", drag_motion)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)

label3.bind("<Button-1>", drag_start)
label3.bind("<B1-Motion>", drag_motion)

root.mainloop()
