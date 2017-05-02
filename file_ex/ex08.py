# .Écrivez un script qui permette d'encoder un fichier texte dont les lignes contiendront
# chacune les noms, prénom, adresse, code postal et no de téléphone de différentes personnes
# (considérez par exemple qu'il s'agit des membres d'un club).

def fill_file():
	name = input('name: ')
	surname = input('surname: ')
	address = input('address: ')
	codep = input('code postal: ')
	phone = input('phone number: ')

	line = "name: {}\nsurname: {}\naddress: {}\ncode postal: {}\nphone number: {}\n".format(name, surname, address, codep, phone)
	fd.write(line)

file = input("member list file: ")
fd = open(file, 'a')
while 1:
	fill_file()
	c = input("add an other member ? (y or n): ")
	if c == 'n':
		break
	fd.write('\n')