"""
ID: mills.n2
LANG: PYTHON3
TASK: combo
"""

inFile = open("combo.in", "r").read().split("\n")
inFile.pop()
outFile = open("combo.out", "w")
#combosFile = open("combo.combos.out", "w")

dialNums = int(inFile.pop(0))
johnCombo = [int(n) for n in inFile.pop(0).split(" ")]
mastCombo = [int(n) for n in inFile.pop(0).split(" ")]

def round_combo(num, maxNumber):
	if num <= 0:
		num = maxNumber + num
	elif num > maxNumber:
		num = (num % maxNumber)

	if num > maxNumber:
		num = maxNumber
	if num <= 0:
		num = 1

	return num

def get_combos(startCombo, maxNumber):
	results = []
	for n1 in range(startCombo[0] - 2, startCombo[0] + 3):
		for n2 in range(startCombo[1] - 2, startCombo[1] + 3):
			for n3 in range(startCombo[2] - 2, startCombo[2] + 3):
				r1 = round_combo(n1, maxNumber)
				r2 = round_combo(n2, maxNumber)
				r3 = round_combo(n3, maxNumber)
				results.append([r1, r2, r3])
	return results

results = []
johnResults = get_combos(johnCombo, dialNums)
mastResults = get_combos(mastCombo, dialNums)

for c in johnResults:
	if not c in results:
		results.append(c)

for c in mastResults:
	if not c in results:
		results.append(c)

#for c in results:
#	combosFile.write(str(c) + "\n")

outFile.write(str(len(results)) + "\n")
outFile.close()
