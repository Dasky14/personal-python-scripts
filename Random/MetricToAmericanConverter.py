from os import system, name
import sys
import math
from decimal import *

input_numbers = Decimal(1)
conversionType = 'None?'
output = ''

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

# --- Conversions ----------------
def decimalRound(value):
	if (value >= 1000):
		return Decimal(round(value))
	else:
		return Decimal('%.3g' % value)

# --- Area -----
def toFootballFields(value):
	value = Decimal(value)
	footballFieldSize = Decimal(5351.215104)
	return '%s' % decimalRound(value / footballFieldSize)

def toPinHeads(value):
	value = Decimal(value)
	pinHeadSize = Decimal(0.00000177)
	return '%s' % decimalRound(value / pinHeadSize)

def toPenniesArea(value):
	value = Decimal(value)
	pennySize = Decimal(0.000285)
	return '%s' % (decimalRound(value / pennySize * Decimal(math.pi / math.sqrt(12))))
# --------------

# --- Volume ---
def toOlympicSwimmingPools(value):
	value = Decimal(value)
	poolSize = Decimal(2500)
	return '%s' % decimalRound(value / poolSize)

def toFluidOunces(value):
	value = Decimal(value)
	mult = Decimal(33814.02270184)
	return '%s' % decimalRound(value * mult)

def toPenniesVolume(value):
	value = Decimal(value)
	pennySize = Decimal(0.00000043323489)
	return '%s' % (decimalRound(value / pennySize * Decimal(math.pi / math.sqrt(12))))
# --------------
# --------------------------------

def askAreaOrVolume():
	global input_numbers
	global conversionType
	
	clear()
	print('Area or volume?')
	print('1. Area')
	print('2. Volume')
	input_char = input()
	conversionType = input_char[0]
	
	clear()
	if (input_char[0] == '1'):
		conversionType = 'Area'
		input_numbers = Decimal(input('Square metres:\n'))
	elif (input_char[0] == '2'):
		conversionType = 'Volume'
		input_numbers = Decimal(input('Cubic metres:\n'))
	else:
		print('*Buzzer sound*')

def askAreaConversion():
	clear()
	print('Select what to convert to:')
	print('1. Football fields')
	print('2. Pin heads')
	print('3. Pennies')
	input_char = input()
	conversionType = input_char[0]
	
	clear()
	global output
	if (input_char[0] == '1'):
		print("Conversion to football fields:")
		output = toFootballFields(input_numbers)
	elif (input_char[0] == '2'):
		print("Conversion to pin heads:")
		output = toPinHeads(input_numbers)
	elif (input_char[0] == '3'):
		print("Conversion to pennies:")
		output = toPenniesArea(input_numbers)
	else:
		print('*Buzzer sound*')

def askVolumeConversion():
	clear()
	print('Select what to convert to:')
	print('1. Olympic swimming pools')
	print('2. Fluid ounces')
	print('3. Pennies')
	input_char = input()
	conversionType = input_char[0]
	
	clear()
	global output
	if (input_char[0] == '1'):
		print("Conversion to olympic swimming pools:")
		output = toOlympicSwimmingPools(input_numbers)
	elif (input_char[0] == '2'):
		print("Conversion to fluid ounces:")
		output = toFluidOunces(input_numbers)
	elif (input_char[0] == '3'):
		print("Conversion to pennies:")
		output = toPenniesVolume(input_numbers)
	else:
		print('*Buzzer sound*')

# --- Main Logic --------------------------

askAreaOrVolume()

if (conversionType == 'Area'):
	askAreaConversion()
elif (conversionType == 'Volume'):
	askVolumeConversion()

print(output)
input() # Wait for enter key to exit