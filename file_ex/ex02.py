# Considérons que vous avez à votre disposition un fichier texte contenant des
# phrases de différentes longueurs. Écrivez un script qui recherche et affiche la phrase la plus longue.

name = input("file name : ")
try:
	fd = open(name, 'r')
except:
	print("file not found")
else:
	longest = ""
	while 1:
		line = fd.readline()
		if line == "":
			break
		elif (len(line) > len(longest)):
			longest = line
	print(longest)
	fd.close()