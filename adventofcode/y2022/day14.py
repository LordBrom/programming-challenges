import sys

class Cave():
	def __init__(self, data) -> None:
		self.rocks = set()
		self.sand = set()
		self.lowestPoint = 0
		self.width = [sys.maxsize, 0]
		self.parse_rocks(data)
		self.dropPoint = [500,0]
		self.sandCount = 0

	def __str__(self) -> str:
		result = ""
		for y in range(self.lowestPoint + 1):
			rowStr = ""
			for x in range(self.width[0], self.width[1]):
				if [x,y] == self.dropPoint:
					rowStr += "+"
				elif f"{x}_{y}" in self.rocks:
					rowStr += "#"
				elif f"{x}_{y}" in self.sand:
					rowStr += "O"
				else:
					rowStr += "."
			result += rowStr + "\n"
		return result

	def parse_rocks(self, data):
		for d in data:
			dSplit = d.split(" -> ")
			point = None
			lastPoint = None
			for p in dSplit:
				point = [int(x) for x in p.split(",")]
				self.lowestPoint = max(self.lowestPoint, point[1])
				self.width[0] = min(self.width[0], point[0])
				self.width[1] = max(self.width[1], point[0])

				if lastPoint != None:
					if point[0] == lastPoint[0]:
						for i in range(min(point[1], lastPoint[1]), max(point[1], lastPoint[1]) + 1):
							self.rocks.add(f"{point[0]}_{i}")
					else:
						for i in range(min(point[0], lastPoint[0]), max(point[0], lastPoint[0]) + 1):
							self.rocks.add(f"{i}_{point[1]}")
				lastPoint = point
		self.lowestPoint += 1
		self.width[0] -= 5
		self.width[1] += 5

	def drop_sand(self, floor = False):
		sandPos = self.dropPoint.copy()
		while True:
			if not floor and sandPos[1] > self.lowestPoint:
				return False
			elif floor and sandPos[1] == self.lowestPoint:
				break

			downPos = f"{sandPos[0]}_{sandPos[1] + 1}"
			leftPos = f"{sandPos[0] - 1}_{sandPos[1] + 1}"
			rightPos = f"{sandPos[0] + 1}_{sandPos[1] + 1}"

			if not downPos in self.rocks and not downPos in self.sand:
				sandPos[1] += 1
				continue

			elif not leftPos in self.rocks and not leftPos in self.sand:
				sandPos[1] += 1
				sandPos[0] -= 1
				continue

			elif not rightPos in self.rocks and not rightPos in self.sand:
				sandPos[1] += 1
				sandPos[0] += 1
				continue

			elif floor and sandPos == self.dropPoint:
				self.sand.add(f"{sandPos[0]}_{sandPos[1]}")
				return False

			break
		self.sand.add(f"{sandPos[0]}_{sandPos[1]}")
		return True


def part1(data, test=False) -> str:
	cave = Cave(data)
	while cave.drop_sand():
		pass
	return str(len(cave.sand))


def part2(data, test=False) -> str:
	cave = Cave(data)
	while cave.drop_sand(True):
		pass
	return str(len(cave.sand))
