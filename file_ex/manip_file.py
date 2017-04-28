from os import *
import pickle

def existe(name):
	global f
	try:
		f = open(name, 'r')
		return 1
	except:
		return 0

name = input("write file name : ")
f = 0
if existe(name):
	print("open success")
	print(f.readlines())
else:
	print("open failure")