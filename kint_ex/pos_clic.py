from tkinter import *

def pointeur(event):
	chaine.configure(text="Clic en position X =" +\
		str(event.x) + "Y =" + str(event.y))
	draw()

def draw():
	global r, col
	cadre.create_oval(event.x - r, event.y - r,\
			event.x + r, event.y + r, fill=col)

col, r = 'red', 10
fen1 = Tk()
cadre = Canvas(fen1, width=400, height=400, bg='light blue')
cadre.bind("<Button-1>", pointeur)
#cadre.bind("<Button-1>", draw)
cadre.pack()
chaine = Label(fen1)
chaine.pack()

fen1.mainloop()