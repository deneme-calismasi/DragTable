from tkinter import *
import time

root = Tk()
root.title("Tarea Programada 2")
root.geometry("800x700+350+100")

fecha = Label(root, text=" ", font=('times', 10), fg='black', bg='white', width=50, height=1)
fecha.place(x=350, y=100)


def horayfecha():
    dia, fecha, mes, ano = time.strftime("%A %m %B %Y").split()

    dias = {'Monday': 'Lunes', 'Tuesday': 'Martes', 'Wednesday': 'Miércoles',
            'Thursday': 'Jueves', 'Friday': 'Viernes', 'Saturday': 'Sábado', 'Sunday': 'Domingo'}

    meses = {'January': 'Enero', 'February': 'Febrero', 'March': 'Marzo', 'April': 'Abril', 'May': 'Mayo',
             'June': 'Junio', 'July': 'Julio', 'August': 'Agosto', 'September': 'Setiembre', 'October': 'Octubre',
             'November': 'Noviembre', 'December': 'Diciembre'}

    return ' '.join(["San José, Costa Rica", dias.get(dia), fecha, "de", meses.get(mes), "de", ano])


fecha.config(text=horayfecha())
root.mainloop()
