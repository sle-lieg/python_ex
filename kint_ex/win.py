from tkinter import *
from random import randrange

# --- Definitions des fonctions gestionnaire d'evenements --- :
def drawLine():
	"tracer ligne"
	global x1, x2, y1, y2, coul
	can1.create_line(x1, y1, x2, y2, width=2, fill=coul)

# --- Modifications des coordonnees pour ligne suivante --- :
	y2, y1 = y2+10, y1-10

def changeColor():
	"changement aleatoire de la couleur"
	global coul
	pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
	c = randrange(8)
	coul = pal[c]

#----- main_prog ----- :
x1, y1, x2, y2 = 10, 190, 190, 10
coul = 'dark green'
# Creation du widget principal :
fen1 = Tk()
# Creation des widgets esclaves :
can1 = Canvas(fen1, bg='dark grey', height=200, width=200)
can1.pack(side=LEFT)
bou1 = Button(fen1, text='Quitter', command=fen1.destroy)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='New line', command=drawLine)
bou2.pack(side=LEFT)
bou3 = Button(fen1, text='Autre couleur', command=changeColor)
bou3.pack(side=BOTTOM)

fen1.mainloop()