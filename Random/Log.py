from os import system, name
import time

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

r = 0
x = 1
sub = True

start_time = time.time()

while True:
	if sub == True:
		r += 1/x
	else:
		r -= 1/x
	x += 1
	sub = not sub
	if (time.time() - start_time) > (1/5):
		start_time = time.time()
		clear()
		print(r)