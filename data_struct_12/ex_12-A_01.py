def copy_file():
	cp = fs.readlines()
	for i in cp:
		dec = i.decode('Latin-1')
		dec = dec.replace(' ', '-*-')
		dec = dec.encode('Utf-8')
		fd.write(dec.title())

sfile = input("source file name: ")
dfile = input("dest file name: ")
try:
	fs = open(sfile, 'rb')
except:
	print("open failure")
else:
	fd = open(dfile, 'wb')
	copy_file()
	fs.close()
	fd.close()