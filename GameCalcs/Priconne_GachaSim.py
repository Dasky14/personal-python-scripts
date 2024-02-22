import sys
import random
import time
from os import system, name

def clear():
	_ = system('cls') if name == 'nt' else system('clear')

def space():
	print("")

# --- Variables --------------------------------------------------------------------

totalAttempts = 5000000
pullsLeft = totalAttempts

oneStarRate = 79.5
twoStarRate = 18
threeStarRate = 2.5
rateUpThreeStarChance = 0.7
rateUpThreeStarCount = 1

oneStars = 0
twoStars = 0
threeStars = 0
rateUpThreeStars = 0

sparkCountNeeded = 300
sparkCount = 0

divineAmulets = 0

# ----------------------------------------------------------------------------------

def printPullsLeft():
	clear()
	print(f"Pulls left: {pullsLeft}")

# --- Main logic -------------------------------------------------------------------

timer = time.perf_counter()
start = timer

pool = []

for _ in range(int(oneStarRate * 100)):
	pool.append("1")

for _ in range(int(twoStarRate * 100)):
	pool.append("2")

for _ in range(int((threeStarRate - rateUpThreeStarChance * rateUpThreeStarCount) * 100)):
	pool.append("3")

for _ in range(int(rateUpThreeStarChance * rateUpThreeStarCount * 100)):
	pool.append("3+")

printPullsLeft()
while pullsLeft > 0:
	if time.perf_counter() - timer >= 1:
		timer = time.perf_counter()
		printPullsLeft()
		print("Pulls per second:", round((totalAttempts - pullsLeft) / (timer - start)))
	
	sparkCount += 1
	pullsLeft -= 1
	
	roll = random.choice(pool)
	
	if roll == "3+":
		rateUpThreeStars += 1
		sparkCount = 0
		divineAmulets += 50
	elif roll == "3":
		threeStars += 1
		divineAmulets += 50
	elif roll == "2":
		twoStars += 1
		divineAmulets += 10
	elif roll == "1":
		oneStars += 1
		divineAmulets += 1
	
	if sparkCount >= sparkCountNeeded:
		rateUpThreeStars += 1
		sparkCount = 0

clear()
print(f"Simulation time                : {round(time.perf_counter() - start, 2)} seconds")
print(f"Total pulls                    : {totalAttempts}")
print(f"Pool size                      : {len(pool)}")
print(f"Pool rate-up 3*                : {pool.count('3+')}")
print(f"Pool 3*                        : {pool.count('3')}")
print(f"Pool 2*                        : {pool.count('2')}")
print(f"Pool 1*                        : {pool.count('1')}")
space()
totalThreeStars = threeStars + rateUpThreeStars
print(f"Total 3*                       : {totalThreeStars}")
print(f"UP 3*                          : {rateUpThreeStars}")
print(f"3* rate                        : {round((totalThreeStars / totalAttempts) * 100, 2)}%")
print(f"UP 3* rate                     : {round((rateUpThreeStars / totalAttempts) * 100, 2)}%")
print(f"Average pulls per 3*           : {round(totalAttempts / totalThreeStars, 2)} pulls")
print(f"Average pulls per UP 3*        : {round(totalAttempts / rateUpThreeStars, 2)} pulls")
print(f"No spark UP 3* average         : {round(1 / ((rateUpThreeStarChance * rateUpThreeStarCount) / 100), 2)} pulls")
space()
print(f"Divine amulets                 : {divineAmulets}")
print(f"Average divine amulets per 10  : {round((divineAmulets / totalAttempts) * 10, 2)}")
input()
