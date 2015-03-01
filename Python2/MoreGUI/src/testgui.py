from tkinter import *

master = Tk()

Label(master, text="first").grid(row=0, column=0)
Label(master, text="second").grid(row=1, column=1)
e1 = Entry(master, width=10)
e1.grid(row=2, column=1)
mainloop()