"""
ID: mills.n2
LANG: PYTHON3
TASK: beads
"""

def rotate_necklace(necklace):
	firstIndex = 0
	firstBead = necklace[firstIndex]
	while firstBead == 'w':
		firstIndex += 1
		firstBead = necklace[firstIndex]

	index = firstIndex + 1
	nextBead = necklace[index]
	while firstBead == nextBead or nextBead == 'w':
		index += 1
		nextBead = necklace[index]
	return necklace[index:] + necklace[0:index]

def color_beads(necklace):
	wPos = necklace.find('w', 0)
	while wPos != -1:
		lIndex = 1
		leftColor = necklace[wPos - lIndex]
		while leftColor == 'w':
			lIndex -= 1
			if wPos - lIndex == len(necklace):
				lIndex = 0
			leftColor = necklace[lIndex]

		rIndex = wPos + 1
		if rIndex == len(necklace):
			rIndex = 0
		rightColor = necklace[rIndex]
		while rightColor == 'w':
			rIndex += 1
			if rIndex == len(necklace):
				rIndex = 0
			rightColor = necklace[rIndex]
		if leftColor == rightColor:
			necklace = necklace[0:wPos] + leftColor + necklace[wPos+1:]
		wPos = necklace.find('w', wPos + 1)
	return necklace

def count_beads(necklace):
	result = []
	currentBead = necklace[0]
	currentCount = 0
	for b in necklace:
		if b == currentBead:
			currentCount += 1
		else:
			if currentBead == 'w':
				result.append('w' + str(currentCount))
			else:
				result.append(currentCount)
			currentBead = b
			currentCount = 1

	if currentBead == 'w':
		result.append('w' + str(currentCount))
	else:
		result.append(currentCount)
	return result


inFile = open("beads.in", "r").read().split("\n")
inFile.pop()
outFile = open("beads.out", "w")
beadCount = int(inFile[0])
necklace = inFile[1]

if necklace.find('r') == -1 or necklace.find('b') == -1:
	result = beadCount
else:
	result = 0

	necklace = color_beads(necklace)

	necklace = rotate_necklace(necklace)

	countedBeads = count_beads(necklace)

	for i in range(len(countedBeads)):
		counted = 0

		firstI = i
		if str(countedBeads[firstI])[0] == 'w':
			counted += int(countedBeads[firstI][1:])
			firstI += 1

		if firstI == len(countedBeads):
			firstI = 0

		counted += countedBeads[firstI]

		nextI = firstI + 1
		if nextI == len(countedBeads):
			nextI = 0
		while str(countedBeads[nextI])[0] == 'w':
			counted += int(countedBeads[nextI][1:])
			nextI += 1
			if nextI == len(countedBeads):
				nextI = 0

		lastI = nextI + 1
		if lastI == len(countedBeads):
			lastI = 0

		while str(countedBeads[lastI])[0] == 'w':
			counted += int(countedBeads[lastI][1:])
			lastI += 1
			if lastI == len(countedBeads):
				lastI = 0
		result = max(result, counted + countedBeads[nextI])

outFile.write(str(min(result, beadCount)) + "\n")
outFile.close()
