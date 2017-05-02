t1 = [31,28,31,30,31,30,31,31,30,31,30,31] 
t2 = [ ' Janvier ' , ' Février ' , ' Mars ' , ' Avril ' , ' Mai ' , ' Juin ' ,
' Juillet ' , ' Août ' , ' Septembre ' , ' Octobre ' , ' Novembre ' , ' Décembre ' ]

j = 0
for i in range(1, 24, 2):
	t2[i:i] = [t1[j]]
	j += 1

t3 = []
t3 = t2[0:len(t2)]

print(t2)
print(t3)
t3[0] = 'hello'
print(t2)
print(t3)