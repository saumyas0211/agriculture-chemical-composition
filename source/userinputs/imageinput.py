import tkinter as tk
from tkinter import *
def measure_dim():
    pass

def measure_health() -> int:
    pass

window = tk.Tk()
window.geometry('800x400')
window.title("IMAGE INPUT")
No = IntVar()
label = Label(window, text="PLANT IMAGE", width=30, justify=LEFT)
entryval = Entry(window, textvariable=No, width=50, justify=RIGHT)
button1 = tk.Button(window, text="PLANT DIMENSIONS", command=measure_dim, width=40, justify=CENTER, pady=10)
button2 = tk.Button(window, text="PLANT HEALTH", command=measure_health, width=40, justify=CENTER, pady=10)
label.grid(row=1, column=1, pady=10)
entryval.grid(row=1, column=2, pady=10)
button1.grid(row=3, column=1, pady=10)
button2.grid(row=3, column=2, pady=10)

window.pack_slaves()
window.mainloop()