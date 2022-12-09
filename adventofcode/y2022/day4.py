
def part1(data, test=False) -> str:
	result = 0
	for d in data:
		dSplit = d.split(",")
		range1 = dSplit[0].split("-")
		range2 = dSplit[1].split("-")

		range1[0] = int(range1[0])
		range1[1] = int(range1[1])
		range2[1] = int(range2[1])
		range2[0] = int(range2[0])

		if range1[1] < range1[0]:
			swap = range1[0]
			range1[0] = range1[1]
			range1[1] = swap

		if range2[1] < range2[0]:
			swap = range2[0]
			range2[0] = range2[1]
			range2[1] = swap

		if range1[0] <= range2[0] and range1[1] >= range2[1]:
			result += 1
		elif range2[0] <= range1[0] and range2[1] >= range1[1]:
			result += 1
	return str(result)


def part2(data, test=False) -> str:
	result = 0
	for d in data:
		dSplit = d.split(",")
		range1 = dSplit[0].split("-")
		range2 = dSplit[1].split("-")

		range1[0] = int(range1[0])
		range1[1] = int(range1[1])
		range2[1] = int(range2[1])
		range2[0] = int(range2[0])

		if range1[1] < range1[0]:
			swap = range1[0]
			range1[0] = range1[1]
			range1[1] = swap

		if range2[1] < range2[0]:
			swap = range2[0]
			range2[0] = range2[1]
			range2[1] = swap

		if range1[0] <= range2[0] and range1[1] >= range2[1]:
			result += 1
		elif range2[0] <= range1[0] and range2[1] >= range1[1]:
			result += 1
		elif range1[0] <= range2[0] and range1[1] >= range2[0]:
			result += 1
		elif range2[0] <= range1[0] and range2[1] >= range1[0]:
			result += 1

	return str(result)
