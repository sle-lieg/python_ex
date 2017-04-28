from tkinter import *

def select_terre():
	global terre, select
	select = terre

def select_mars():
	global mars, select
	select = mars

def teleport(event):
	global select, tx, ty, tr, mx, my, mr
	if select == terre:
		tx, ty = event.x, event.y
		can1.coords(select, event.x-tr, event.y-tr, event.x+tr, event.y+tr)
		msg.configure(text='Coordonnees de la planete terre: ['+str(tx)+';'+str(ty)+']')
	else:
		mx, my = event.x, event.y
		can1.coords(select, event.x-mr, event.y-mr, event.x+mr, event.y+mr)
		msg.configure(text='Coordonnees de la planete mars: ['+str(mx)+';'+str(my)+']')

def move(rl, ud):
	global select, tx, ty, tr, mx, my, mr
	if select == terre:
		tx, ty = tx+rl, ty+ud
		can1.coords(select, tx-tr, ty-tr, tx+tr, ty+tr)
		msg.configure(text='Coordonnees de la planete terre: ['+str(tx)+';'+str(ty)+']')	
	else:
		mx, my = mx+rl, my+ud
		can1.coords(select, mx-mr, my-mr, mx+mr, my+mr)
		msg.configure(text='Coordonnees de la planete mars: ['+str(mx)+';'+str(my)+']')

def move_up():
	move(0, -10)

def move_down():
	move(0, 10)

def move_left():
	move(-10, 0)

def move_rigth():
	move(10, 0)
#----- main ------ :

#variables:
tx, ty, tr, mx, my, mr = 100, 100, 30, 300, 300, 20

# Creation fenetres:
fen1 = Tk()
fen1.title("10.G: ex1")
can1 = Canvas(fen1, bg='black', height=400, width=400)
can1.grid(row=0, rowspan=50)
can1.bind("<Button-1>", teleport)

#creation d'un label:
msg = Label(fen1, text='Coordonnees de la planete terre: ['+str(tx)+';'+str(ty)+']')
msg.grid(row=50, column=0)

# Creation boutons:
Button(fen1, text='terre', command=select_terre).grid(row=0, column=1, sticky=W)
Button(fen1, text='mars', command=select_mars).grid(row=0, column=3, sticky=W)
Button(fen1, text=chr(0x2190), command=move_left).grid(row=4, column=1, sticky=N)
Button(fen1, text=chr(0x2191), command=move_up).grid(row=3, column=2, sticky=N)
Button(fen1, text=chr(0x2192), command=move_rigth).grid(row=4, column=3, sticky=N)
Button(fen1, text=chr(0x2193), command=move_down).grid(row=5, column=2, sticky=N)

# Creation planetes:
terre = can1.create_oval(tx-tr, ty-tr, tx+tr, ty+tr, fill='light blue')
mars = can1.create_oval(mx-mr, my-mr, mx+mr, my+mr, fill='red')
select = terre

fen1.mainloop()