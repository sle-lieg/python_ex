from random import *

cards = ['as de coeur','Deux de coeur','trois de coeur','Quatre de coeur','Cinq de coeur',
		'Six de coeur','Sept de coeur','Huit de coeur','Neuf de coeur','Dix de coeur',
		'Valet de coeur','Dame de coeur','Roi de coeur']

i, l = 0, len(cards)
while i < l:
	new = cards[i].replace('coeur', 'trefle')
	cards.append(new)
	new = cards[i].replace('coeur', 'pique')
	cards.append(new)
	new = cards[i].replace('coeur', 'carreau')
	cards.append(new)
	i += 1

print(cards)

while 1:
	n = input('tapez <Enter> pour tirer une carte:')
	if n != '':
		break
	print(choice(cards))