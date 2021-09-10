"""
ID: mills.n2
LANG: PYTHON3
TASK: transform
"""
import copy

inFile = open("transform.in", "r").read().split("\n")
inFile.pop()
outFile = open("transform.out", "w")
sideLength = int(inFile.pop(0))

startPattern = []
endPattern = []

def print_pattern(pattern):
	for i in pattern:
		print((' ').join(i))
	print("")

def check_pattern(start, end):
	for i in range(len(start)):
		for j in range(len(start[i])):
			if (start[i][j] != end[i][j]):
				return False
	return True

def rotate_pattern_90_clockwise(pattern):
	result = copy.deepcopy(pattern)

	for i in range(len(pattern)):
		for j in range(len(pattern[i])):
			result[j][i] = pattern[i][j]

	return reflected_pattern_horizontally(result)

def reflected_pattern_horizontally(pattern):
	result = copy.deepcopy(pattern)

	for r in result:
		r.reverse()

	return result

def split(word):
	return [char for char in word]

for i in range(sideLength):
	startPattern.append(split(inFile.pop(0)))

for i in range(sideLength):
	endPattern.append(split(inFile.pop(0)))

modifiedPattern = copy.deepcopy(startPattern)

operationResult = 0
for i in range(7):
	operationResult += 1
	if operationResult == 1 or operationResult == 2 or operationResult == 3:
		modifiedPattern = rotate_pattern_90_clockwise(modifiedPattern)
		if (check_pattern(endPattern, modifiedPattern)):
			break
	elif operationResult == 4:
		modifiedPattern = copy.deepcopy(startPattern)
		modifiedPattern = reflected_pattern_horizontally(modifiedPattern)
		if (check_pattern(endPattern, modifiedPattern)):
			break
	elif operationResult == 5:
		found = False
		for i in range(3):
			modifiedPattern = rotate_pattern_90_clockwise(modifiedPattern)
			if (check_pattern(endPattern, modifiedPattern)):
				found = True
				break
		if found:
			break
	elif operationResult == 6:
		if (check_pattern(endPattern, startPattern)):
			break

outFile.write(str(operationResult) + '\n')
outFile.close()
