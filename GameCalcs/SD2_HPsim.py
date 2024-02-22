import sys
import math
from prettytable import PrettyTable
from os import system, name

def clear():
	_ = system('cls') if name == 'nt' else system('clear')

def levelUpCost(currentLevel: int):
    return max(math.pow(currentLevel, 1.3), 1)

breakpoints = []

usedEssence = 0
nextPoint = 1000000


hpLevel = 1
classLevels = [1, 1, 1, 1]

# [class relic index, damage reduction]
classInfo = [[0, 0.72],
             [1, 0.77],
             [1, 0.77],
             [1, 0.77],
             [2, 0.72],
             [3, 0.25]]

classCount = len(classLevels)


while len(breakpoints) < 8:
    
    hpCost = levelUpCost(hpLevel)
    classEfficiency = float("inf")
    classCost = 0
    efficientClass = 0
    for i in range(len(classLevels)):
        levelCost = levelUpCost(classLevels[i])
        totalEffHp = 0
        for char in classInfo:
            if char[0] != i:
                continue
            totalEffHp += (2 / (1 - char[1]))
        eff = levelCost / totalEffHp

        if eff < classEfficiency:
            classEfficiency = eff
            classCost = levelCost
            efficientClass = i

    hpTotalEffHp = 0
    for char in classInfo:
        hpTotalEffHp += (5 / (1 - char[1]))
    hpEfficiency = hpCost / hpTotalEffHp

    if classEfficiency < hpEfficiency:
        classLevels[efficientClass] += 1
        usedEssence += classCost
    else:
        hpLevel += 1
        usedEssence += hpCost

    if usedEssence >= nextPoint:
        nextPoint *= 10
        breakpoints.append([usedEssence, hpLevel, classLevels.copy()])


clear()

table = PrettyTable()
table.field_names = ["Essence used", "HP relic", "Class relics", "HP to class", "Class to hp"]

# Left align all fields
for field_name in table.field_names:
    table.align[field_name] = "l"

for data in breakpoints:
    table.add_row([str(round(data[0])), 
                str(data[1]), 
                str(data[2]), 
                str(round(data[1] / (sum(data[2]) / len(data[2])), 2)),
                str(round((sum(data[2]) / len(data[2])) / data[1], 2))])

print(table)