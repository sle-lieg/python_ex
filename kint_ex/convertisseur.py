from tkinter import *
from math import *

def convert_C_to_F(event):
	entree_F.delete(0, 20)
	entree_F.insert(0, str(float(eval(entree_C.get()) * 9/5 + 32)))

def convert_F_to_C(event):
	entree_C.delete(0, 20)
	entree_C.insert(0, str((float(entree_F.get()) - 32) * 5/9))


# ------ main ----- :
fen1 = Tk()
val1 = Label(fen1, text="degres Celsius      :")
val2 = Label(fen1, text="degres Fahrenheit :")

entree_C = Entry(fen1)
entree_C.bind("<KeyRelease>", convert_C_to_F)
entree_F = Entry(fen1)
entree_F.bind("<KeyRelease>", convert_F_to_C)


val1.grid(sticky=W)
val2.grid(row=1, sticky=W)
entree_C.grid(row=0, column=1, sticky=E)
entree_F.grid(row=1, column=1, sticky=E)

fen1.mainloop()
