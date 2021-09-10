import tkinter.ttk as ttk
from tkinter import *

import numpy as np
import pandas as pd

root = Tk()
data1 = [{'Sensor No': 5}, {'Sensor No': 6}, {'Sensor No': 7}, {'Sensor No': 8}, {'Sensor No': 9}, {'Sensor No': 10}]
df = pd.DataFrame.from_records(data1)

sensor_no = np.array(df['Sensor No'])

button_dict = {}


def callback_function(x): print('Pressed:', x)


for index, dat in enumerate(sensor_no):
    button = ttk.Button(root, text=dat,
                        command=lambda dat=dat: callback_function(dat))
    button.grid(row=index + 1, column=1, pady=0, padx=0)
    button_dict[dat] = button  # Stores a reference to the button under
    # the name from the database

for name in sensor_no:
    print(name, button_dict[name])  # prints all button/name associations

root.mainloop()
