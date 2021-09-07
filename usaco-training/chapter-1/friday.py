"""
ID: mills.n2
LANG: PYTHON3
TASK: friday
"""

inFile = open("friday.in", "r").read().split("\n")
inFile.pop()
outFile = open("friday.out", "w")
yearCap = int(inFile[0])

monthLengths = [31,28,31,30,31,30,31,31,30,31,30,31]
result = [0,0,0,0,0,0,0]

yearIndex = 1900
monthIndex = 0
dowIndex = 2

dowIndex += 12
dowIndex %= 7
result[dowIndex] += 1

for y in range(yearCap):
	currentYear = 1900 + y
	for i in range(len(monthLengths)):
		if currentYear == 1900 + (yearCap - 1) and i == 11:
			break
		currentMonthLength = monthLengths[i]
		if (i == 1 and currentYear % 4 == 0 and (currentYear % 100 != 0 or currentYear % 400 == 0)):
			currentMonthLength += 1
		dowIndex += currentMonthLength
		dowIndex %= 7
		result[dowIndex] += 1

firstOut = True
for r in result:
	if not firstOut:
		outFile.write(" ")
	outFile.write(str(r))
	firstOut = False

outFile.write("\n")
outFile.close()
