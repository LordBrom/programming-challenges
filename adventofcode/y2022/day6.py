
def part1(data, test=False, charCount=4) -> str:
	for i in range(charCount, len(data[0])):
		check = data[0][i-charCount:i]
		found = []
		bad = False
		for l in check:
			if l in found:
				bad = True
				break
			found.append(l)
		if not bad:
			return str(i)
	return "not implemented"


def part2(data, test=False) -> str:
	return part1(data, test, 14)
