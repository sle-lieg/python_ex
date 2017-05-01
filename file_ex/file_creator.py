import os

def r_file():
	try:
		fd = open(name, 'r')
	except:
		print("file not found.")
		return
	else:
		line = fd.read()
		print(line)
	fd.close()

def ecrire_file():
	fd = open(name, 'a')
	while 1:
		line = input()
		if line == '':
			break
		else:
			fd.write(line)
	fd.close()

name = input("entrer nom de fichier: ")
print("1: ecrire dans le fichier\n2: lire le fichier\n")
while 1:
	mode = int(input("selection : "))
	if mode == 1:
		ecrire_file()
		break
	elif mode == 2:
		r_file()
		break
	else:
		print("select 1 ou 2.\n")
