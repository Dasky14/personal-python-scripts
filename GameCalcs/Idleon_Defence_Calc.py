from os import system, name
import math

def clear():
	_ = system('cls') if name == 'nt' else system('clear')

def main():
    clear()
    defence = float(input("Input defence: "))
    damage = float(input("Input damage: "))

    result = (damage - 2.5 * defence ** 0.8) / max(1, 1 + (defence ** 2.5 / max (100, 100 * damage)))
    print("{0:.1f}".format(result))
    input("Enter to exit...")

main()