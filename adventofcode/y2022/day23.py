import sys
ORDER = [0,1,2,3]

class Elf():
	def __init__(self, x, y) -> None:
		self.x = x
		self.y = y
		self.moveDir = None
		self.moveTo = None

	def __eq__(self, __o: object) -> bool:
		return isinstance(__o, Elf) and __o.x == self.x and __o.y == self.y

	def choose_move(self, grid):
		neighbors = grid.get_neighbors(self.x, self.y)
		noElves = True
		for n in neighbors:
			if n != None:
				noElves = False
				break
		if noElves:
			#print("no elves")
			return False

		for o in ORDER:
			if o == 0:
				if neighbors[0] == None and neighbors[1] == None and neighbors[7] == None:
					#print("wants to move N")
					self.moveTo = [self.x - 1, self.y]
					return True

			elif o == 1:
				if neighbors[4] == None and neighbors[3] == None and neighbors[5] == None:
					#print("wants to move S")
					self.moveTo = [self.x + 1, self.y]
					return True

			elif o == 2:
				if neighbors[6] == None and neighbors[7] == None and neighbors[5] == None:
					#print("wants to move W")
					self.moveTo = [self.x, self.y - 1]
					return True

			elif o == 3:
				if neighbors[2] == None and neighbors[1] == None and neighbors[3] == None:
					#print("wants to move E")
					self.moveTo = [self.x, self.y + 1]
					return True

	def do_move(self, elves):
		for e in elves:
			if self != e and self.moveTo == e.moveTo:
				return False
		self.x = self.moveTo[0]
		self.y = self.moveTo[1]
		return True


class Grid():
	def	__init__(self, gridSize = 1000) -> None:
		self.grid = []
		self.elves = []
		for x in range(gridSize):
			self.grid.append([None for y in range(gridSize)])

	def __str__(self) -> str:
		result = ""
		for x, row in enumerate(self.grid):
			rowStr = ""
			for y, p in enumerate(row):
				if p == None:
					rowStr += "."
				else:
					rowStr += "#"
			result += rowStr + "\n"
		return result

	def add_elf(self, elf):
		self.grid[elf.x][elf.y] = elf
		self.elves.append(elf)

	def turn(self):
		global ORDER
		noMoves = True
		for elf in self.elves:
			if elf.choose_move(self):
				pass

		for elf in self.elves:
			ox, oy = elf.x, elf.y
			if elf.do_move(self.elves):
				noMoves = False
				self.grid[elf.x][elf.y] = self.grid[ox][oy]
				self.grid[ox][oy] = None

		for elf in self.elves:
			elf.moveTo = None

		tomove = ORDER[0]
		ORDER = ORDER[1:]
		ORDER.append(tomove)

		return noMoves





	def get_neighbors(self, x, y):
		adjacent = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
		neighbors = []
		for dx, dy in adjacent:
			nx, ny = x + dx, y + dy
			if 0 <= nx < len(self.grid[0]) and 0 <= ny < len(self.grid):
				neighbors.append(self.grid[nx][ny])
			else:
				neighbors.append(None)
		return neighbors

	def part_1_result(self):
		xAxis = [sys.maxsize, 0]
		yAxis = [sys.maxsize, 0]
		for elf in self.elves:
			xAxis[0] = min(xAxis[0], elf.x)
			xAxis[1] = max(xAxis[1], elf.x)

			yAxis[0] = min(yAxis[0], elf.y)
			yAxis[1] = max(yAxis[1], elf.y)

		return ((xAxis[1] - xAxis[0] + 1) * (yAxis[1] - yAxis[0] + 1)) - len(self.elves)



def make_grid(data):
	grid = Grid()
	offset = 300
	for i,d in enumerate(data):
		for j,p in enumerate(d):
			if p == "#":
				grid.add_elf(Elf(i + offset, j + offset))
	return grid



def part1(data, test=False) -> str:
	grid = make_grid(data)
	for i in range(10):
		grid.turn()
	return str(grid.part_1_result())


def part2(data, test=False) -> str:
	global ORDER
	ORDER = [0,1,2,3]
	grid = make_grid(data)
	result = 1
	while not grid.turn():
		result += 1

	return str(result)
