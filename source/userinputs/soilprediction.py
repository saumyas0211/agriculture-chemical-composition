import tkinter as tk
from tkinter import *

def android_soilinput() -> int:
    pass

window = tk.Tk()
window.geometry('800x400')
window.title("IMAGE INPUT")
No = IntVar()
label = Label(window, text="SOIL Mg", width=30, justify=LEFT)
entryval = Entry(window, textvariable=No, width=50, justify=RIGHT)
label1 = Label(window, text="SOIL Potassium(K)", width=30, justify=LEFT)
entryval1 = Entry(window, textvariable=No, width=50, justify=RIGHT)
label2 = Label(window, text="SOIL Nitrogen(N)", width=30, justify=LEFT)
entryval2 = Entry(window, textvariable=No, width=50, justify=RIGHT)
label3 = Label(window, text="SOIL pH", width=30, justify=LEFT)
entryval3 = Entry(window, textvariable=No, width=50, justify=RIGHT)
button2 = tk.Button(window, text="DEVICE INPUT", command=android_soilinput, width=40, justify=CENTER, pady=10)
label.grid(row=1, column=1, pady=10)
entryval.grid(row=1, column=2, pady=10)
label1.grid(row=2, column=1, pady=10)
entryval1.grid(row=2, column=2, pady=10)
label2.grid(row=3, column=1, pady=10)
entryval2.grid(row=3, column=2, pady=10)
label3.grid(row=4, column=1, pady=10)
entryval3.grid(row=4, column=2, pady=10)
button2.grid(row=5, column=2, pady=10)
window.pack_slaves()
window.mainloop()