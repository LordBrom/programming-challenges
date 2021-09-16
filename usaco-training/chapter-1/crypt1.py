"""
ID: mills.n2
LANG: PYTHON3
TASK: crypt1
"""

import math

inFile = open("crypt1.in", "r").read().split("\n")
inFile.pop()
outFile = open("crypt1.out", "w")

numOfNums = inFile.pop(0)
allowedNums = [int(n) for n in inFile.pop(0).split(" ")]

solutions = 0

def verify_number(num, allowedNums, numLen):
	while num != 0:
		numLen -= 1
		digit = num % 10
		num = math.floor(num / 10)
		if not digit in allowedNums:
			return False
	return numLen == 0

topNums = []

for i in allowedNums:
	for j in allowedNums:
		for k in allowedNums:
			topNums.append(i + (j * 10) + (k * 100))

for i in topNums:
	for n in allowedNums:
		p1 = i * n
		if not verify_number(p1, allowedNums, 3):
			continue
		for m in allowedNums:
			p2 = i * m
			if not verify_number(p2, allowedNums, 3):
				continue
			s = p1 + (p2 * 10)
			if verify_number(s, allowedNums, 4):
				solutions += 1

outFile.write(str(solutions) + "\n")
outFile.close()
