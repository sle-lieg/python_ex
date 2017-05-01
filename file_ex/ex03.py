name = input("file name : ")
fd = open(name, 'a')
for t in range(2, 31):
	for i in range(1, 21):
		line = "{} * {} = {}\n".format(t, i, t*i)
		fd.write(line)
	fd.write('\n')
fd.close()