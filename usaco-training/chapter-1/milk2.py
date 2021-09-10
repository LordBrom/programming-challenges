"""
ID: mills.n2
LANG: PYTHON3
TASK: milk2
"""

inFile = open("milk2.in", "r").read().split("\n")
inFile.pop()
outFile = open("milk2.out", "w")

farmerCount = inFile.pop(0)

schedule = [0] * 1000000

for i in inFile:
	times = i.split(" ")
	start = int(times[0])
	end = int(times[1])
	schedule[start:end] = [1] * (end - start)

maxMilking = 0
maxIdle = 0

tempMilking = 0
tempIdle = 0
countingMilking = False
countingIdle = False

hasStarted = False

for i in schedule:
	if i == 0:
		if not hasStarted:
			continue
		if countingMilking:
			countingMilking = False
			maxMilking = max(maxMilking, tempMilking)
			tempMilking = 0
		countingIdle = True
		tempIdle += 1
	else:
		hasStarted = True
		if countingIdle:
			countingIdle = False
			maxIdle = max(maxIdle, tempIdle)
			tempIdle = 0
		countingMilking = True
		tempMilking += 1

outFile.write(str(maxMilking) + " " + str(maxIdle) + '\n')
outFile.close()
