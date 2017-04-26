i = 1
while i <= 20:
	r = i * 7
	print(r, end=" ")
	if(r % 3 == 0):
		print("*", end=" ")
	i += 1
print()