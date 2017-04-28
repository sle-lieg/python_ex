from tkinter import *
from math import *

def rotate():
	global rl, ud, x, y
	angle = 10
	x += cos(angle) * 10
	y += sin(angle) * 10

	if x >= 260:
		x = 260
		rl = -rl
	if x <= 0:
		x = 0
		rl = -rl
	if y >= 260:
		y = 260
		ud = -ud
	if y <= 0:
		y = 0
		ud = -ud
	can1.coords(oval1, x, y, x+40, y+40)

def move():
	global rl, ud, x, y
	x, y = x+rl, y+ud
	if x >= 260:
		x = 260
		rl = -rl
	if x <= 0:
		x = 0
		rl = -rl
	if y >= 260:
		y = 260
		ud = -ud
	if y <= 0:
		y = 0
		ud = -ud
	can1.coords(oval1, x, y, x+40, y+40)


#----- main ------ :
x, y, ud, rl = 100, 50, 10, 10

fen1 = Tk()
can1 = Canvas(fen1, height=300, width=300, bg='black')
can1.pack(side=TOP)
oval1 = can1.create_oval(x, y, x+40, y+40, fill='red')
bou1 = Button(fen1, text='move', command=rotate)
bou1.pack(side=BOTTOM)


fen1.mainloop()