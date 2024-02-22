import sys
import math
from prettytable import PrettyTable
from os import system, name

def clear():
	_ = system('cls') if name == 'nt' else system('clear')

# --- Static Numbers ---
baseCritDmg = 0.5
baseCritRate = 0.05
critRateCap = 1
# ----------------------

def calculateDamage(cRate: float, cDmg: float):
    critDamage = baseCritDmg + cDmg
    return critDamage * min(cRate + baseCritRate, critRateCap)

def addRow(t: PrettyTable, cR: float, cD: float):
    global baseCritDmg
    global baseCritRate
    t.add_row([str(round((cR + cD) * 100)) + '%',
               str(round(cR * 100)) + '%',
               str(round(cD * 100)) + '%',
               str(round((baseCritRate + cR) * 100)) + '%',
               str(round ((baseCritDmg + cD) * 100)) + '%',
               str(round(calculateDamage(cR, cD) * 100, 1)) + '%'])


table = PrettyTable()
table.field_names = ["Total Stats", "Extra Rate", "Extra Damage", "Final Rate%", "Final Dmg%", "DPS increase"]

# Left align all fields
for field_name in table.field_names:
    table.align[field_name] = "l"

critRate = 0
critDamage = 0

addRow(table, 0, 0)

rowCount = 1
additions = 0
while rowCount < 20:
    chanceEff = calculateDamage(critRate + 0.01, critDamage)
    damageEff = calculateDamage(critRate, critDamage + 0.01)

    if chanceEff >= damageEff:
        critRate += 0.01
    else:
        critDamage += 0.02
    additions += 1
    
    if additions % 10 == 0:
        rowCount += 1
        addRow(table, critRate, critDamage)
        

print(table)
input()