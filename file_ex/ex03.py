name = input("file name : ")
fd = open(name, 'a')
for t in range(2, 30):
	for i in range(1, 20):
		line = str(t) + '*' + str(i) + '=' + str(t*i) + '\n'
		fd.write(line)
fd.close()