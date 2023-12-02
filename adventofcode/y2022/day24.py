from collections import deque
import copy

RIGHT = 1
DOWN = 2
LEFT = 3
UP = 4


class Valley():
	def __init__(self, data) -> None:
		self.start = None
		self.end = None
		self.grid = []
		self.minute = 0
		self.pos = None
		for x,d in enumerate(data):
			gridRow = []
			for y,p in enumerate(d):
				if x == 0 and p == ".":
					self.start = (x, y)
				elif x == len(data) - 1 and p == ".":
					self.end = (x, y)

				if p == "#":
					gridRow.append(False)
				elif p == ".":
					gridRow.append([])
				elif p == ">":
					gridRow.append([RIGHT])
				elif p == "v":
					gridRow.append([DOWN])
				elif p == "<":
					gridRow.append([LEFT])
				elif p == "^":
					gridRow.append([UP])
			self.grid.append(gridRow)

	def __lt__(self, other):
		return self.grid < other.grid

	def __str__(self) -> str:
		result = ""
		for x,row in enumerate(self.grid):
			rowStr = ""
			for y,p in enumerate(row):
				if p == False:
					rowStr += "#"
				elif (x,y) == self.pos:
					rowStr += "C"
				elif (x,y) == self.start:
					rowStr += "S"
				elif (x,y) == self.end:
					rowStr += "E"
				elif len(p) == 0:
					rowStr += "."
				elif len(p) > 1:
					rowStr += str(len(p))

				elif p[0] == RIGHT:
					rowStr += ">"
				elif p[0] == DOWN:
					rowStr += "v"
				elif p[0] == LEFT:
					rowStr += "<"
				elif p[0] == UP:
					rowStr += "^"
			result += rowStr + "\n"
		return result

	def move_blizzards(self):
		nextGrid = self.blank_valley()
		for x,row in enumerate(self.grid):
			for y,p in enumerate(row):
				if p == False:
					continue
				for b in p:
					nx, ny = self.next_step(b, x, y)
					nextGrid[nx][ny].append(b)

		self.grid = nextGrid
		self.minute += 1
		return self

	def next_step(self, dir, x, y):
		nx, ny = x, y
		if dir == RIGHT:
			ny += 1
		elif dir == DOWN:
			nx += 1
		elif dir == LEFT:
			ny -= 1
		elif dir == UP:
			nx -= 1

		if nx == 0:
			nx = len(self.grid) - 2

		elif nx == len(self.grid) - 1:
			nx = 1

		if ny == 0:
			ny = len(self.grid[0]) - 2

		if ny == len(self.grid[0]) - 1:
			ny = 1

		return nx, ny



	def blank_valley(self):
		result = []
		for x,row in enumerate(self.grid):
			gridRow = []
			for y,p in enumerate(row):
				if p == False:
					gridRow.append(False)
				else:
					gridRow.append([])
			result.append(gridRow)
		return result


def getNeighbors(x, y, h, w):
	adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
	neighbors = []
	for dx, dy in adjacent:
		nx, ny = x + dx, y + dy
		if 0 <= nx < w and 0 <= ny < h:
			neighbors.append((nx, ny))
	return neighbors

def find_path(blizzard, start, end, time):
	queue = deque()
	visited = set()


	while True:
		while not queue:
			time += 1
			if is_open(blizzard, *start, time):
				queue.append((*start, time))

		x, y, t = queue.popleft()

		if (x, y, t) in visited:
			continue
		visited.add((x, y, t))

		if (x, y) == end:
			return t

		for nx, ny in getNeighbors(x, y, blizzard['cols'], blizzard['rows']):
			if is_open(blizzard, nx, ny, t):
				queue.append((nx, ny, t + 1))

def is_open(b, x, y, t):
	return not any((
		(x, (y - t) % b['cols']) in b['right'],
		(x, (y + t) % b['cols']) in b['left'],
		((x - t) % b['rows'], y) in b['down'],
		((x + t) % b['rows'], y) in b['up'],
	))


def parse_input(data):
	lines = [line[1:-1] for line in data[1:-1]]
	blizzard = {
		'rows': len(lines),
		'cols': len(lines[0]),
		'right': [(x, y) for x in range(len(lines)) for y in range(len(lines[0])) if lines[x][y] == ">"],
		'down': [(x, y) for x in range(len(lines)) for y in range(len(lines[0])) if lines[x][y] == "v"],
		'left': [(x, y) for x in range(len(lines)) for y in range(len(lines[0])) if lines[x][y] == "<"],
		'up': [(x, y) for x in range(len(lines)) for y in range(len(lines[0])) if lines[x][y] == "^"]
	}
	return blizzard

def part1(data, test=False) -> str:
	blizzard = parse_input(data)
	start = (0, 0)
	end = (blizzard['rows'] - 1, blizzard['cols'] - 1)
	return str(find_path(blizzard, start, end, 0))


def part2(data, test=False) -> str:
	blizzard = parse_input(data)
	start = (0, 0)
	end = (blizzard['rows'] - 1, blizzard['cols'] - 1)
	there = find_path(blizzard, start, end, 0)
	back = find_path(blizzard, end, start, there)
	again = find_path(blizzard, start, end, back)
	return str(again)
