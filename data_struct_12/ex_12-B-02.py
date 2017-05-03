from random import *

while 1:
	n = input("nombre de valeurs a tirer aleatoirement: ")
	if n == '':
		n = 1000
		break
	else:
		try:
			n = int(n)
		except:
			print('enter only numeric caracteres.')
		else:
			if n < 1 or n > 1000:
				print('number between 1 and 1000.')
			else:
				break

t = []
i = 0
while i < n:
	t.append(random())
	i+=1

while 1:
	fract = input('nombre de fractions: ')
	try:
		fract = int(fract)
	except:
		print('enter only numeric caracteres.')
	else:
		if fract < 1 or fract > 10:
			print('number between 1 and 10.')
		else:
			break

piv = [1 / fract]*fract
i = 1
while i < fract:
	piv[i] += piv[i-1]
	i += 1

compt = [0]*fract
for e in t:
	i = 0
	while i < fract:
		if e < piv[i]:
			compt[i] += 1
			break
		i += 1
print(t)
print(compt)