from os import system, name
import sys
import random
import time
string = ""
trycount = 0

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

start_time = time.time()

while string != "Hello World":
	string = ""
	trycount += 1
	for x in range(11):
		string += "Hello World"[random.randint(0,10)]
	
	if (time.time() - start_time) > (1/2) or string == "Hello World":
		clear()
		print("Attempting to randomly write \"Hello World\"")
		print(string, " ", trycount)
		start_time = time.time()

print("Found Hello World in " , trycount , "tries!")