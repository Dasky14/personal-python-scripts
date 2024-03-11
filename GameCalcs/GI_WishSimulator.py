import sys
import random
import time
from os import system, name


def clear():
    _ = system("cls") if name == "nt" else system("clear")


def space():
    print("")


# --- Variables --------------------------------------------------------------------

totalAttempts = 5000000
pullsLeft = totalAttempts

fiveStarPity = 0
fourStarPity = 0
fiveStarRateUpPity = False
fourStarRateUpPity = False

fiveStars = 0
rateUpFiveStars = 0
fourStars = 0
rateUpFourStars = 0
threeStars = 0

fiveStarChance = 0.6
fourStarChance = 5.1

fiveStarGuarantee = 90
fourStarGuarantee = 10

# ----------------------------------------------------------------------------------


def pulledFiveStar():
    global fiveStarRateUpPity
    global rateUpFiveStars
    global fiveStars
    global fiveStarPity
    global fourStarPity

    rateUp = bool(random.getrandbits(1))

    if rateUp or fiveStarRateUpPity:
        fiveStarRateUpPity = False
        rateUpFiveStars += 1
    else:
        fiveStarRateUpPity = True

    fiveStars += 1

    fiveStarPity = 0
    fourStarPity = 0


def pulledFourStar():
    global fourStarRateUpPity
    global rateUpFourStars
    global fourStars
    global fourStarPity

    rateUp = bool(random.getrandbits(1))

    if rateUp or fourStarRateUpPity:
        fourStarRateUpPity = False
        rateUpFourStars += 1
    else:
        fourStarRateUpPity = True

    fourStars += 1

    fourStarPity = 0


def printPullsLeft():
    clear()
    print("Pulls left:", pullsLeft)


# --- Main logic -------------------------------------------------------------------

pool = []

for i in range(round(fiveStarChance * 10)):
    pool.append(5)

for i in range(round(fourStarChance * 10)):
    pool.append(4)

for i in range(1000 - len(pool)):
    pool.append(3)

timer = time.perf_counter()
start = timer

printPullsLeft()
while pullsLeft > 0:
    if time.perf_counter() - timer >= 1:
        timer = time.perf_counter()
        printPullsLeft()
        print("Pulls per second:", round((totalAttempts - pullsLeft) / (timer - start)))

    fiveStarPity += 1
    fourStarPity += 1

    roll = random.choice(pool)

    if roll == 5:
        pulledFiveStar()
    elif fiveStarPity >= fiveStarGuarantee:
        pulledFiveStar()
    elif roll == 4:
        pulledFourStar()
    elif fourStarPity >= fourStarGuarantee:
        guaranteedPull = random.choice(pool)
        if guaranteedPull == 5:
            pulledFiveStar()
        else:
            pulledFourStar()
    elif roll == 3:
        threeStars += 1

    pullsLeft -= 1

clear()
print("Simulation time          :", round(time.perf_counter() - start, 2), "seconds")
print("Total pulls              :", totalAttempts)
print("Pool size                :", len(pool))
print("Pool 5*                  :", round(fiveStarChance * 10))
print("Pool 4*                  :", round(fourStarChance * 10))
space()
print("Total 5*                 :", fiveStars)
print("UP 5*                    :", rateUpFiveStars)
print(
    "5* rate                  :", str(round((fiveStars / totalAttempts) * 100, 2)) + "%"
)
print(
    "UP 5* rate               :",
    str(round((rateUpFiveStars / totalAttempts) * 100, 2)) + "%",
)
print("Average pulls per 5*     :", str(round(totalAttempts / fiveStars, 2)) + " pulls")
print(
    "Average pulls per UP 5*  :",
    str(round(totalAttempts / rateUpFiveStars, 2)) + " pulls",
)
space()
print("Total 4*                 :", fourStars)
print("UP 4*                    :", rateUpFourStars)
print(
    "4* rate                  :", str(round((fourStars / totalAttempts) * 100, 2)) + "%"
)
print(
    "UP 4* rate               :",
    str(round((rateUpFourStars / totalAttempts) * 100, 2)) + "%",
)
print("Average pulls per 4*     :", str(round(totalAttempts / fourStars, 2)) + " pulls")
print(
    "Average pulls per UP 4*  :",
    str(round(totalAttempts / rateUpFourStars, 2)) + " pulls",
)
space()
print("Total 3*                 :", threeStars)
input()
