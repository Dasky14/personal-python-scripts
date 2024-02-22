from os import system, name
import time

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

printFreq = 1
lastPrint = time.time()
iters = 0

sum = 1
div = 3
add = False
while True:
	if add == True:
		sum += 1 / div
	else:
		sum -= 1 / div
	
	add = not add
	div += 2
	
	iters += 1
	if time.time() - lastPrint > printFreq:
		lastPrint = time.time()
		clear()
		print(sum * 4)
		print('Iterations: ' , iters)