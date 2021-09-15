"""
ID: mills.n2
LANG: PYTHON3
TASK: barn1
"""

inFile = open("barn1.in", "r").read().split("\n")
inFile.pop()
outFile = open("barn1.out", "w")

firstLineSplit = inFile.pop(0).split(" ")
maxBoards = int(firstLineSplit[0])
stalls = int(firstLineSplit[1])
cows = int(firstLineSplit[2])

barnStalls = "0" * stalls
blockedStalls = "0" * stalls

def set_barn_cover(barn, start, end, cover = "1"):
	for i in range(start, end + 1):
		barn = barn[:i] + cover + barn[i+1:]
	return barn

def longest_gaps(barn, start, end, gapCount):
	result = []

	i = start
	while i < end + 1:
		if barn[i] == "1":
			i += 1
			continue
		j = i + 1
		while barn[j] == "0" and j < end + 1:
			j += 1
		j -= 1
		if len(result) < gapCount:
			result.append([j - i, i, j])
		else:
			result.sort(key=lambda x: x[0])
			for r in range(len(result)):
				if j - i > result[r][0]:
					result[r] = [j - i, i, j]
					break
		i = j + 1
	return result

for c in inFile:
	barnStalls = barnStalls[:int(c)] + "1" + barnStalls[int(c)+1:]

firstCow = barnStalls.index("1")
lastCow = barnStalls.rindex("1")

blockedStalls = set_barn_cover(blockedStalls, firstCow, lastCow)

gaps = longest_gaps(barnStalls, firstCow, lastCow, maxBoards - 1)

for g in gaps:
	blockedStalls = set_barn_cover(blockedStalls, g[1], g[2], "0")

result = 0
for s in blockedStalls:
	if s == "1":
		result += 1

outFile.write(str(result) + "\n")
outFile.close()
