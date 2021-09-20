"""
ID: mills.n2
LANG: PYTHON3
TASK: wormhole
"""

from itertools import permutations

def next_wormhole(wormholes, startPos):
	result = -1
	distance = 0
	for n in range(len(wormholes)):
		if wormholes[n][1] == startPos[1] and wormholes[n][0] > startPos[0]:
			if wormholes[n][0] - startPos[0] < distance or distance == 0:
				result = n
				distance = wormholes[n][0] - startPos[0]
	return result

#I feel like there must be a better way to do this, but I just can't think of it.
def get_connections(holeCount):
	perm = list(permutations(range(holeCount)))
	result = []
	for p in perm:
		isValid = True
		for i in range(len(p)):
			if i == p[i] or i != p[p[i]]:
				isValid = False
				break
		if isValid:
			result.append(p)
	return result


inFile = open("wormhole.in", "r").read().split("\n")
inFile.pop()
outFile = open("wormhole.out", "w")

wormholeCount = int(inFile.pop(0))
wormholes = []
for n in range(wormholeCount):
	wormhole = inFile.pop(0).split(" ")
	wormholes.append([int(wormhole[0]), int(wormhole[1])])


connections = get_connections(len(wormholes))
holesToTheRight = []
for hole in wormholes:
	holesToTheRight.append(next_wormhole(wormholes, hole))


result = 0
for c in range(len(connections)):
	con = connections[c]
	for i in range(len(wormholes)):
		loopFound = False
		visited = [False] * len(wormholes)
		hole = wormholes[i]
		pos = i
		while pos != -1:
			if visited[pos]:
				result += 1
				loopFound = True
				break
			visited[pos] = True
			pos = holesToTheRight[con[pos]]
		if loopFound:
			break


outFile.write(str(result) + '\n')
outFile.close()
