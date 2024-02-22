import os

def calcPi(limit):
	q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

	decimal = limit
	counter = 0

	while counter != decimal + 1:
		if 4 * q + r - t < n * t:
			# yield digit
			yield n
			# insert period after first digit
			if counter == 0:
				yield '.'
			# end
			if decimal == counter:
				print('')
				break
			counter += 1
			nr = 10 * (r - n * t)
			n = ((10 * (3 * q + r)) // t) - 10 * n
			q *= 10
			r = nr
		else:
			nr = (2 * q + r) * l
			nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
			q *= k
			t *= l
			l += 2
			k += 1
			n = nn
			r = nr


def main():  # Wrapper function

	# Calls CalcPi with the given limit
	pi_digits = calcPi(int(input(
		"Enter the number of decimals to calculate to: ")))

	os.remove("pi.txt")
	file = open("pi.txt", "a+")
	
	i = 0
	fileOutput = ""
	# Prints the output of calcPi generator function
	# Inserts a newline after every 40th number
	for d in pi_digits:
			fileOutput += str(d)
			print(d, end='')
			i += 1
			if i == 40:
				file.write(fileOutput + "\n")
				fileOutput = ""
				print("")
				i = 0
	file.write(fileOutput)

	file.close()

if __name__ == '__main__':
	main()