def fill_dico():
	global dico
	while 1:
		while 1:
			ex = input('Enregistrer une nouvelle personne ? (y or n): ')
			if ex == 'n':
				return
			elif ex == 'y':
				break
		name = input('name: ')
		age = input('age: ')
		size = input('taille: ')
		if name == '' or size == '' or age == '' :
			print('missing information.')
		else:
			dico[name] = (int(age), float(size))

def read_dico():
	global dico
	while 1:
		print('\nchoisissez un nom de membre parmis la liste: ', end='[')
		for e in dico.keys():
			print('|', e, sep='', end='|')
		key = input(']\nname: ')
		if key == '':
			break
		if key in dico:
			val = dico[key]
			print('Nom: {} - age: {} - taille: {}'.format(key, val[0], val[1]))


global dico
dico = {}

fill_dico()
read_dico()