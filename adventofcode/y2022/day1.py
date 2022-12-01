
def part1(data, test=False) -> str:
	elves = [0]
	for n in data:
		if n == "":
			elves.append(0)
			continue
		elves[-1] += int(n)

	elves.sort()
	return str(elves[-1])


def part2(data, test=False) -> str:
	elves = [0]
	for n in data:
		if n == "":
			elves.append(0)
			continue
		elves[-1] += int(n)

	maxElf = 0
	for e in elves:
		maxElf = max(e, maxElf)

	elves.sort()
	return str(elves[-1] + elves[-2] + elves[-3])
