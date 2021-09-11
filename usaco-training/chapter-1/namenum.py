"""
ID: mills.n2
LANG: PYTHON3
TASK: namenum
"""

NAMES = open("dict.txt", "r").read().split("\n")
inFile = open("namenum.in", "r").read().split("\n")
inFile.pop()
outFile = open("namenum.out", "w")

tagNumber = inFile[0]

lookUp = [[], [], ['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'], ['P','R','S'], ['T','U','V'], ['W','X','Y']]

letterOptions = []
AVAILABLENAMES = []

for num in tagNumber:
	letterOptions.append(lookUp[int(num)])

def get_names(letterOptions, index = 0, name=""):
	if (index >= len(letterOptions)):
		if name in NAMES:
			AVAILABLENAMES.append(name)
		return

	for l in letterOptions[index]:
		get_names(letterOptions, index + 1, name + l)

	return

get_names(letterOptions)

for name in sorted(AVAILABLENAMES):
	outFile.write(name.upper() + '\n')
if len(AVAILABLENAMES) == 0:
	outFile.write('NONE\n')

outFile.close()
