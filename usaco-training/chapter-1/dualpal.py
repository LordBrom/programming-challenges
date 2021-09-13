"""
ID: mills.n2
LANG: PYTHON3
TASK: dualpal
"""

inFile = open("dualpal.in", "r").read().split("\n")
inFile.pop()
outFile = open("dualpal.out", "w")
inputSplit = inFile.pop(0).split(" ")
outputCount = int(inputSplit[0])
startNum = int(inputSplit[1])
endNum = 10000


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

numToCheck = startNum
while outputCount != 0:
	numToCheck += 1
	found = False
	for base in range(2, 11):
		numInBase = "".join(numberToBase(numToCheck, base))
		if (is_pal(numInBase)):
			if not found:
				found = True
			else:
				outFile.write(str(numToCheck) + "\n")
				outputCount -= 1
				break
	if outputCount == 0:
		break

outFile.close()
