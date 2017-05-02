# À partir de deux fichiers préexistants A et B, construisez un fichier C qui contienne
# alternativement un élément de A, un élément de B, un élément de A... et ainsi de suite
# jusqu'à atteindre la fin de l'un des deux fichiers originaux. Complétez ensuite C avec
# les éléments restant sur l'autre

def mix_files():
	while 1:
		line1 = fs1.readline()
		line2 = fs2.readline()
		if line1 == '' and line2 == '':
			break
		if line1 != '':
			fd.write(line1)
		if line2 != '':
			fd.write(line2)

file1 = input("name file1: ")
file2 = input("name file2: ")
file3 = input("name file3: ")

try:
	fs1 = open(file1, 'r')
	fs2 = open(file2, 'r')
except:
	print("open failure")
else:
	fd = open(file3, 'w')
	mix_files()
	fs1.close()
	fs2.close()
	fd.close()