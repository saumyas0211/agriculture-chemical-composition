import tkinter as tk
from tkinter import *
def measure_nutrients():
    pass

def measure_water() -> int:
    pass

window = tk.Tk()
window.geometry('800x400')
window.title("IMAGE INPUT")
No = IntVar()
label = Label(window, text="SOIL IMAGE", width=30, justify=LEFT)
entryval = Entry(window, textvariable=No, width=50, justify=RIGHT)
button1 = tk.Button(window, text="SOIL SPECTRUM", command=measure_nutrients, width=40, justify=LEFT, pady=10)
button2 = tk.Button(window, text="SOIL HEALTH", command=measure_water, width=40, justify=CENTER, pady=10)
label.grid(row=1, column=1, pady=10)
entryval.grid(row=1, column=2, pady=10)
button1.grid(row=3, column=1, pady=10)
button2.grid(row=3, column=2, pady=10)
window.pack_slaves()
window.mainloop()