from tkinter import *
from math import *

def moving_snake():
	global snake_l, cote, width
	for elem in snake_l:
		elem[1] = elem[1] + cote
		can1.coords(elem[0], elem[1], elem[2], elem[1]+cote, elem[2]+cote)
		if elem[1] >= width:
			elem[1] = 0
	fen1.after(100, moving_snake)

def draw_snake():
	global cote, snake_l
	snake_l.append((can1.create_rectangle(cote*5, cote*3, cote*5 + cote, cote*3 + cote, fill='red'), cote*5, cote*3))
	snake_l.append((can1.create_rectangle(cote*4, cote*3, cote*4 + cote, cote*3 + cote, fill='red'), cote*4, cote*3))
	snake_l.append((can1.create_rectangle(cote*3, cote*3, cote*3 + cote, cote*3 + cote, fill='red'), cote*3, cote*3))

#----- main ----- :
cote = 15
snake_l = []
height, width = cote*30, cote*30

#----- fenetre et fond principal ----- :
fen1 = Tk()
fen1.title("test de jeux")
can1 = Canvas(fen1, height=height, width=width, relief='raised', bd=5, bg='light blue')
can1.pack(side=TOP)

#----- serpent ----- :
draw_snake()
print(snake_l)
moving_snake()

fen1.mainloop()
