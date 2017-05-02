# Écrivez un script qui compare les contenus de deux fichiers et signale la première différence rencontrée

def find_diff():
	global line1, line2
	i = 0
	while line1[i] == line2[i]:
		i += 1
	print(line1[i], line2[i])

file1 = input("file1 name: ")
file2 = input("file2 name: ")
try:
	sf1 = open(file1, 'r')
	sf2 = open(file2, 'r')
except:
	print('open failure')
else:
	while 1:
		line1 = sf1.readline()
		line2 = sf2.readline()
		if line1 == '' and line2 == '':
			print("file identicals")
			break
		else:
			if line1 != line2:
				find_diff()
				break
	sf1.close()
	sf2.close()