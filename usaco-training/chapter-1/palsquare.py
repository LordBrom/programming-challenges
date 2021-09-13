"""
ID: mills.n2
LANG: PYTHON3
TASK: palsquare
"""

inFile = open("palsquare.in", "r").read().split("\n")
inFile.pop()
outFile = open("palsquare.out", "w")
base = int(inFile.pop(0))

def is_pal(num):
	reverseNum = str(num)[::-1]
	return str(num) == reverseNum

def numberToBase(n, b):
	numToLetter = ['A','B','C','D','E','F','G','H','I','J','K','L','M']
	if n == 0:
		return [0]
	digits = []
	while n:
		nextDigit = int(n % b)
		if nextDigit > 9:
			digits.append(numToLetter[nextDigit - 10])
		else:
			digits.append(str(int(n % b)))
		n //= b
	return digits[::-1]

for i in range(300):
	numToCheck = i + 1
	powToCheck = pow(numToCheck, 2)
	numInBase = "".join(numberToBase(numToCheck, base))
	powInBase = "".join(numberToBase(powToCheck, base))

	if (is_pal(powInBase)):
		outFile.write(str(numInBase) + " " + str(powInBase) + "\n")

outFile.close()
