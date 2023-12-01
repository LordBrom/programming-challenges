def is_visible(forrest, treePos):
	treeHeight = forrest[treePos[0]][treePos[1]]

	visible = True
	for i in range(treePos[0]):
		if treeHeight <= forrest[i][treePos[1]]:
			visible = False

	if visible:
		return True

	visible = True
	for i in range(treePos[0] + 1, len(forrest)):
		if treeHeight <= forrest[i][treePos[1]]:
			visible = False

	if visible:
		return True


	visible = True
	for i in range(treePos[1]):
		if treeHeight <= forrest[treePos[0]][i]:
			visible = False

	if visible:
		return True

	visible = True
	for i in range(treePos[1] + 1, len(forrest[0])):
		if treeHeight <= forrest[treePos[0]][i]:
			visible = False

	if visible:
		return True


	return False

def get_score(forrest, treePos):
	totalScore = 1
	treeHeight = forrest[treePos[0]][treePos[1]]

	score = 0
	for i in reversed(range(treePos[0])):
		score += 1
		if treeHeight <= forrest[i][treePos[1]]:
			break
	totalScore *= score

	score = 0
	for i in range(treePos[0] + 1, len(forrest)):
		score += 1
		if treeHeight <= forrest[i][treePos[1]]:
			break
	totalScore *= score


	score = 0
	for i in reversed(range(treePos[1])):
		score += 1
		if treeHeight <= forrest[treePos[0]][i]:
			break
	totalScore *= score

	score = 0
	for i in range(treePos[1] + 1, len(forrest[0])):
		score += 1
		if treeHeight <= forrest[treePos[0]][i]:
			break
	totalScore *= score


	return totalScore

def part1(data, test=False) -> str:
	visibleTrees = (len(data) * 2) + ((len(data) - 2) * 2)
	for row in range(1, len(data) - 1):
		for col in range(1, len(data[row]) - 1):
			if is_visible(data, [row, col]):
				visibleTrees += 1
	return str(visibleTrees)


def part2(data, test=False) -> str:
	best = 0
	for row in range(1, len(data) - 1):
		for col in range(1, len(data[row]) - 1):
			score = get_score(data, [row, col])
			best = max(best, score)
	return str(best)
