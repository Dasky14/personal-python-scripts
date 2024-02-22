from os import system, name
import sys
import random
import time

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')


string = "World Hello"
array = list(string)
trycount = 0

start_time = time.time()

while "".join(array) != "Hello World":
	trycount += 1
	random.shuffle(array)
	if (time.time() - start_time) > (1/10) or "".join(array) == "Hello World":
		clear()
		print("Attempting to randomly write \"Hello World\"")
		print("".join(array), " ", trycount)
		start_time = time.time()

print("Found Hello World in " , trycount , "tries!")
