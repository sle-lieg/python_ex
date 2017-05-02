# Vous avez à votre disposition un fichier texte dont chaque ligne est
# la représentation d'une valeur numérique de type réel (mais sans exposants):
# Écrivez un script qui recopie ces valeurs dans un autre fichier en les
# arrondissant en nombres entiers (l'arrondi doit être correct)

sfile = input("source file name: ")
dfile = input("dest file name: ")
try:
	sf = open(sfile, 'r')
except:
	print('open failure')
else:
	df = open(dfile, 'w')
	while 1:
		line = sf.readline()
		if line == '':
			break
		else:
			df.write(str(round(float(line))))
			df.write('\n')
	sf.close()
	df.close()