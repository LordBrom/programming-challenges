"""
ID: mills.n2
LANG: PYTHON3
TASK: namenum
"""

names = open("dict.txt", "r").read().split("\n")
inFile = open("namenum.in", "r").read().split("\n")
inFile.pop()
outFile = open("namenum.out", "w")

tagNumber = inFile[0]

lookUp = [[], [], ['A','B','C'], ['D','E','F'], ['G','H','I'], ['J','K','L'], ['M','N','O'], ['P','R','S'], ['T','U','V'], ['W','X','Y']]

LETTEROPTIONS = []

for num in tagNumber:
	LETTEROPTIONS.append(lookUp[int(num)])

def filterNames(name):
	if (len(LETTEROPTIONS) != len(name)):
		return False

	for i in range(len(name)):
		if (not name[i] in LETTEROPTIONS[i]):
			return False

	return True

namesAvailable = filter(filterNames, names)

found = False
for name in sorted(namesAvailable):
	found = True
	outFile.write(name.upper() + '\n')
if not found:
	outFile.write('NONE\n')

outFile.close()
