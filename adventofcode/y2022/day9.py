class SnakeBridge():

	def __init__(self, steps, segments=1) -> None:
		self.snake = [[0,0] for x in range(segments + 1)]
		self.steps = steps

		self.size = 25
		self.result = 0
		self.tailVisits = []

	def __str__(self):
		result = ""
		for row in range(self.size):
			rowStr = ""
			for col in range(self.size):
				tailCheck = self.check_tail_pos([row, col])
				if [row,col] == self.snake[0]:
					rowStr += "H "
				elif tailCheck != None:
					rowStr += f"{tailCheck} "
				elif row == 0 and col == 0:
					rowStr += "s "
				else:
					rowStr += ". "
			result += rowStr + "\n"
		return result

	def check_tail_pos(self, pos):
		for i,val in enumerate(self.snake):
			if self.snake[i] == pos:
				if i == len(self.snake) - 1:
					return "T"
				return i


	def run(self):
		for d in self.steps:
			dSplit = d.split(" ")
			dir = dSplit[0]
			steps = dSplit[1]
			for i in range(int(steps)):
				if dir == "R":
					self.snake[0][1] += 1
				elif dir == "U":
					self.snake[0][0] += 1
				elif dir == "L":
					self.snake[0][1] -= 1
				elif dir == "D":
					self.snake[0][0] -= 1

				for i in range(len(self.snake) - 1):
					self.move_segment(i, i+1)

				if not f'{self.snake[-1][0]}_{self.snake[-1][1]}' in self.tailVisits:
					self.tailVisits.append(f'{self.snake[-1][0]}_{self.snake[-1][1]}')

	def move_segment(self, headSeg, tailSeg):
		if max(abs(self.snake[headSeg][0] - self.snake[tailSeg][0]), abs(self.snake[tailSeg][1] - self.snake[headSeg][1])) > 1:
			if self.snake[headSeg][0] == self.snake[tailSeg][0]:
				if self.snake[headSeg][1] > self.snake[tailSeg][1]:
					self.snake[tailSeg][1] += 1
				else:
					self.snake[tailSeg][1] -= 1

			elif self.snake[headSeg][1] == self.snake[tailSeg][1]:
				if self.snake[headSeg][0] > self.snake[tailSeg][0]:
					self.snake[tailSeg][0] += 1
				else:
					self.snake[tailSeg][0] -= 1
			else:
				if self.snake[headSeg][0] > self.snake[tailSeg][0]:
					self.snake[tailSeg][0] += 1
				else:
					self.snake[tailSeg][0] -= 1

				if self.snake[headSeg][1] > self.snake[tailSeg][1]:
					self.snake[tailSeg][1] += 1
				else:
					self.snake[tailSeg][1] -= 1




def part1(data, test=False) -> str:
	snakeBridge = SnakeBridge(data)
	snakeBridge.run()
	return str(len(snakeBridge.tailVisits))


def part2(data, test=False) -> str:
	snakeBridge = SnakeBridge(data, 9)
	snakeBridge.run()
	return str(len(snakeBridge.tailVisits))
