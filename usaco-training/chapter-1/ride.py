"""
ID: mills.n2
LANG: PYTHON2
TASK: ride
"""

inFile = open("ride.in", "r").read().split("\n")
inFile.pop()
outFile = open("ride.out", "w")

solution = [0, 0]
index = 0

def text_to_num(line):
	val = 1
	for letter in line:
		val *= ord(letter) - 64
	return val

for line in inFile:
	solution[index] = text_to_num(line)
	index += 1

if (solution[0] % 47 == solution[1] % 47):
	outFile.write('GO\n')
else:
	outFile.write('STAY\n')

outFile.close()
