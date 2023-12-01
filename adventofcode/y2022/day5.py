
def part1(data, test=False) -> str:
	stacks = []
	while data[0] != "":
		d = data.pop(0)
		for i in range(1, len(d) - 1):
			if d[i - 1] == "[" and d[i + 1] == "]":
				stackNum = int((i - 1) / 4)
				while len(stacks) <= stackNum:
					stacks.append("")
				stacks[stackNum] = d[i] + stacks[stackNum]
		if d == "":
			break

	data.pop(0)
	for d in data:
		dparsed = d.replace("move ", "").replace(" from ", ",").replace(" to ", ",")
		dSplit = dparsed.split(",")
		dSplit[0] = int(dSplit[0])
		dSplit[1] = int(dSplit[1]) - 1
		dSplit[2] = int(dSplit[2]) - 1
		for i in range(dSplit[0]):
			stacks[dSplit[2]] += stacks[dSplit[1]][-1:]
			stacks[dSplit[1]] = stacks[dSplit[1]][:-1]

	result = ""
	for s in stacks:
		result += s[-1]
	return result


def part2(data, test=False) -> str:
	stacks = []
	while data[0] != "":
		d = data.pop(0)
		for i in range(1, len(d) - 1):
			if d[i - 1] == "[" and d[i + 1] == "]":
				stackNum = int((i - 1) / 4)
				while len(stacks) <= stackNum:
					stacks.append("")
				stacks[stackNum] = d[i] + stacks[stackNum]
		if d == "":
			break

	data.pop(0)
	for d in data:
		dparsed = d.replace("move ", "").replace(" from ", ",").replace(" to ", ",")
		dSplit = dparsed.split(",")
		dSplit[0] = int(dSplit[0])
		dSplit[1] = int(dSplit[1]) - 1
		dSplit[2] = int(dSplit[2]) - 1
		stacks[dSplit[2]] += stacks[dSplit[1]][-dSplit[0]:]
		stacks[dSplit[1]] = stacks[dSplit[1]][:-dSplit[0]]

	result = ""
	for s in stacks:
		result += s[-1]
	return result
