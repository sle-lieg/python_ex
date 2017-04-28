from tkinter import *
from math import *

def moving_snake():
	global snake_l, cote, width
	x = 0
	for (snake_l[x]) in snake_l:
		snake_l[x][1] = snake_l[x][1] + (cote)
		can1.coords(snake_l[x][0], snake_l[x][1], snake_l[x][2], snake_l[x][1]+cote, snake_l[x][2]+cote)
		if snake_l[x][1] >= width:
			snake_l[x][1] = 0
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
