#Écrivez un script qui génère automatiquement un fichier texte contenant les 
#tables de multiplication de 2 à 30 (chacune d'entre elles incluant 20 termes seulement)

name = input("file name : ")
fd = open(name, 'a')
for t in range(2, 31):
	for i in range(1, 21):
		line = "{} * {} = {}\n".format(t, i, t*i)
		fd.write(line)
	fd.write('\n')
fd.close()