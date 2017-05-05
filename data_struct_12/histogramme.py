occu = {}
file = input('file name: ')
try:
	fd = open(file, 'r')
except:
	print('file not found.')
else:
	lines = fd.readlines()
	for e in lines:
		tmp = list(e)
		for i in range(len(tmp)):
			if not tmp[i].isalnum():
				tmp[i] = ' '
		tmp = ''.join(tmp)
		tmp = tmp.split()
		for e in tmp:
			occu[e] = occu.get(e, 0) + 1
	print(occu)
