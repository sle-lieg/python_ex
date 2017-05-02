# -*- coding:Utf-8 -*-

line = "ceci est une longue phrase a decouper en plusieurs morceaux de 5 charactere et a rassemblez dans l' ordre inverse par la suite"
t = []
lon = len(line)
part = 0
while part < lon:
	t.append(line[part:part+5])
	part += 5
part = 1
new = ''
while part <= len(t):
	new += str(t[-part])
	part += 1
print(t)
print(new)
