def load_dic(cur_dic):
	file = input('file to load: ')
	try:
		fd = open(file, 'r')
	except:
		print('file not found')
	else:
		while 1:
			line = fd.readline()
			if line == '':
				break
			line = line.split('@')
			val = tuple((line[1].strip()).split('#'))
			cur_dic[line[0]] = val
		fd.close()

def write_dic(cur_dic):
	while 1:
		name = input('name: ')
		age = input('age: ')
		taille = input('taille: ')
		if name == '' or age == '' or taille == '':
			print('informations manquantes pour ajouter au dictionnaire.')
		else:
			cur_dic[name] = (int(age), float(taille))
			while 1:
				choix = input('enregistrer un nouveau membre ? (y-n) ').upper()
				if choix == 'Y':
					break
				elif choix == 'N':
					return
				else:
					print("'y' ou 'n'")

def read_dic(cur_dic):
	if not cur_dic:
		print('le dictionnaire est vide.')
	else:
		while 1:
			key = input('nom de la personne ou <Enter> to main menu: ')
			if key == '':
				break
			if key in cur_dic:
				val = cur_dic[key]
				print('nom: {} - age: {} - taille: {}'.format(key, val[0], val[1]))
			else:
				print('nom introuvable.')

def save_dic(cur_dic):
	name = input('nom du fichier de sauvegarde (<Enter> pour annuler): ')
	if name == '':
		return
	while 1:
		mode = input("mode d' ouverture : (A)ppend, (E)crase: ").lower()
		if mode == 'a':
			fd = open(name, 'a')
			break
		elif mode == 'e':
			fd = open(name, 'w')
			break
		else:
			print("mauvais mode d' ouverture entrer.")
	for key, val in cur_dic.items():
		line = '{}@{}#{}\n'.format(key, val[0], val[1])
		fd.write(line)
	fd.close()

def exit_prog(cur_dic):
	exit(0)

def wrong_choice(cur_dic):
	print('mauvais choix.')

#----- main ------
funct_dic, cur_dic = {}, {}
funct_dic['R'] = load_dic
funct_dic['A'] = write_dic
funct_dic['C'] = read_dic
funct_dic['S'] = save_dic
funct_dic['T'] = exit_prog

while 1:
	print('\n---------- MENU -----------')
	print('(R)ecuperer un dictionnaire depuis un fichier')
	print('(A)jouter des donnees au dictionnaire courant')
	print('(C)onsulter le dictionnaire courant')
	print('(S)auvegarder le dictionnaire courant dans un fichier')
	print('(T)erminer')
	choix = input().upper()
	funct_dic.get(choix, wrong_choice)(cur_dic)
#	print(cur_dic)