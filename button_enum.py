from tkinter import *

root = Tk()

files = []  # creates list to replace your actual inputs for troubleshooting purposes
button = []  # creates list to store the buttons ins

for i in range(6):  # this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
    files.append("Button " + str(i))

for i in range(len(files)):  # this says for *counter* in *however many elements there are in the list files*
    # the below line creates a button and stores it in an array we can call later, it will print the value of it's own text by referencing itself from the list that the buttons are stored in
    button.append(Button(root, text=files[i], command=lambda c=i: print(button[c].cget("text"))))
    button[i].pack()  # this packs the buttons

root.mainloop()
