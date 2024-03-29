from tkinter import *
 
#procedure generale de deplacement :
def avance(gd, hb):
	global x1, y1
	x1, y1 = x1 + gd, y1 + hb
	can1.coords(oval1, x1, y1, x1+30, y1+30)

#gestionnaire d'evenement :
def depl_gauche():
	avance(-10, 0)

def depl_droit():
	avance(10, 0)

def depl_haut():
	avance(0, -10)

def depl_bas():
	avance(0, 10)

#------ Programme main ----- :
x1, y1 = 10, 10

#	Creation du widget principal ("maitre"):
fen1 = Tk()
fen1.title("Exercice d'animation avec tkinter")

#	creation des widget "esclave":
can1 = Canvas(fen1, bg='dark grey', height=300, width=300)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
can1.pack(side=LEFT)
Button(fen1, text='Quitter', command=fen1.quit).pack(side=BOTTOM)
Button(fen1, text='Gauche', command=depl_gauche).pack()
Button(fen1, text='Droite', command=depl_droit).pack()
Button(fen1, text='Haut', command=depl_haut).pack()
Button(fen1, text='Bas', command=depl_bas).pack()

fen1.mainloop()