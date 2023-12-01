

# 1 = rock
# 2 = paper
# 3 = Scissors
def score_round(player, op):
	score = player

	if player == op:
		score += 3
	elif player == 1 and op == 3:
		score += 6
	elif player == 2 and op == 1:
		score += 6
	elif player == 3 and op == 2:
		score += 6

	return score

def part1(data, test=False) -> str:
	score = 0
	player = {
		"X": 1,
		"Y": 2,
		"Z": 3,
	}
	op = {
		"A": 1,
		"B": 2,
		"C": 3,
	}
	for d in data:
		dSplit = d.split(" ")
		score += score_round(player[dSplit[1]], op[dSplit[0]])
	return str(score)

def part2(data, test=False) -> str:
	score = 0
	op = {
		"A": 1,
		"B": 2,
		"C": 3,
	}
	for d in data:
		dSplit = d.split(" ")
		playerPlay = 1
		if dSplit[1] == "X":
			playerPlay = op[dSplit[0]] - 1
			if playerPlay == 0:
				playerPlay = 3
		elif dSplit[1] == "Y":
			playerPlay = op[dSplit[0]]
		else:
			playerPlay = op[dSplit[0]] + 1
			if playerPlay == 4:
				playerPlay = 1

		score += score_round(playerPlay, op[dSplit[0]])
	return str(score)
