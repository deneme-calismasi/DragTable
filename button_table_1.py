import tkinter as tk

window = tk.Tk()
window.geometry('800x600')
placeX = 20
placeY = 20
bl = []


def direction(type_):
    pass


class SideBar():
    def __init__(self):
        global window
        global placeX
        global placeY
        global bl
        self.name = []
        self.placeX = placeX
        self.placeY = placeY
        self.bl = []
        self.bl.append(self.name)

    def create_folder(self, index, name):
        self.name.append(name)
        self.bl.append(tk.Button(window, text=self.name[-1], command=lambda: direction(self.name)))
        self.bl[-1].config(height=3, width=6)
        self.bl[-1].place(x=self.placeX, y=self.placeY)
        self.placeY += 100


side_bar = SideBar()
# Documents = SideBar('Documents')

side_bar.create_folder(0, 'Computer')
side_bar.create_folder(1, 'Documents')

window.mainloop()
