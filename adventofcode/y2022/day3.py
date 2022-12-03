import math

def part1(data, test=False) -> str:
	total = 0
	for d in data:
		sackOne = d[:math.floor(len(d)/2)]
		sackTwo = d[math.floor(len(d)/2):]

		for l in sackOne:
			if l in sackTwo:
				if ord(l) > 91:
					total += ord(l) - 96
				else:
					total += (ord(l) - 64) + 26
				break

	return str(total)


def part2(data, test=False) -> str:
	total = 0
	for i in range(int(len(data) / 3)):
		for l in data[i * 3]:
			if l in data[(i * 3) + 1] and l in data[(i * 3) + 2]:
				if ord(l) > 91:
					total += ord(l) - 96
				else:
					total += (ord(l) - 64) + 26
				break

	return str(total)
