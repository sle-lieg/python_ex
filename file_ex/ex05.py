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