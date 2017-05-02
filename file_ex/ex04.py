#Écrivez un script qui recopie un fichier texte en triplant tous les espaces entre les mots

sfile = input("source file name: ")
dfile = input("dest file name: ")
try:
	sf = open(sfile, 'r')
except:
	print('open failure')
else:
	df = open(dfile, 'w')
	while 1:
		old = sf.readline()
		if old == '':
			break
		else:
			old = old.split()
			new = '   '.join(old)
			df.write(new)
			df.write('\n')
	sf.close()
	df.close()