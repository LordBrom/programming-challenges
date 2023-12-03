import re
import traceback

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

class Map():
	def __init__(self, data) -> None:
		self.map = []
		self.pos = None
		self.facing = RIGHT
		self.path = [set() for x in range(4)]


		mapRow = data.pop(0)
		while mapRow != "":
			if self.pos == None:
				self.pos = [0,mapRow.index(".")]
			self.map.append([0 if x == "." else 1 if x == "#" else 2 for x in mapRow])
			mapRow = data.pop(0)
		self.movement = re.findall('[0-9]+.', data.pop(0))

	def __str__(self) -> str:
		result = ""
		for x in range(len(self.map)):
			rowStr = ""
			for y in range(len(self.map[x])):
				if self.map[x][y] == 2:
					rowStr += " "
				elif [x, y] == self.pos:
					rowStr += ['R', 'D', 'L', 'U'][self.facing]
				elif f"{x}_{y}" in self.path[0]:
					rowStr += ">"
				elif f"{x}_{y}" in self.path[1]:
					rowStr += "V"
				elif f"{x}_{y}" in self.path[2]:
					rowStr += "<"
				elif f"{x}_{y}" in self.path[3]:
					rowStr += "^"
				elif self.map[x][y] == 1:
					rowStr += "#"
				elif self.map[x][y] == 0:
					rowStr += "."
			result += rowStr + "\n"
		return result

	def move(self):
		for move in self.movement:
			if move[-1] in ['L', 'R']:
				steps = int(move[:-1])
				dir = move[-1]
			else:
				steps = int(move)
				dir = None
			for i in range(steps):
				self.path[self.facing].add(f'{self.pos[0]}_{self.pos[1]}')
				nx, ny = self.next_tile()
				if nx < 0 or ny < 0 or nx > len(self.map) - 1 or ny > len(self.map[nx]) - 1 or self.map[nx][ny] == 2:
					ox, oy = self.opposite_tile()
					if self.map[ox][oy] == 1:
						break
					else:
						self.pos = [ox, oy]
				elif self.map[nx][ny] == 1:
					break
				else:
					self.pos = [nx, ny]
			self.turn(dir)

	def turn(self, dir):
		if self.facing == UP:
			if dir == "L":
				self.facing = LEFT
			elif dir == "R":
				self.facing = RIGHT

		elif self.facing == RIGHT:
			if dir == "L":
				self.facing = UP
			elif dir == "R":
				self.facing = DOWN

		elif self.facing == DOWN:
			if dir == "L":
				self.facing = RIGHT
			elif dir == "R":
				self.facing = LEFT

		elif self.facing == LEFT:
			if dir == "L":
				self.facing = DOWN
			elif dir == "R":
				self.facing = UP

	def next_tile(self):
		if self.facing == UP:
			return self.pos[0] - 1, self.pos[1]

		elif self.facing == RIGHT:
			return self.pos[0], self.pos[1] + 1

		elif self.facing == DOWN:
			return self.pos[0] + 1, self.pos[1]

		elif self.facing == LEFT:
			return self.pos[0], self.pos[1] - 1

	def opposite_tile(self):
		if self.facing == UP:
			for x in reversed(range(len(self.map))):
				if self.pos[1] > len(self.map[x]):
					continue
				if self.map[x][self.pos[1]] in [0,1]:
					tileXPos = x
					break
			return tileXPos, self.pos[1]

		elif self.facing == RIGHT:
			tileYPos = min(self.map[self.pos[0]].index(0), self.map[self.pos[0]].index(1))
			return self.pos[0], tileYPos

		elif self.facing == DOWN:
			for x in range(len(self.map)):
				if self.map[x][self.pos[1]] in [0,1]:
					tileXPos = x
					break
			return tileXPos, self.pos[1]

		elif self.facing == LEFT:
			tileYPos = min(list(reversed(self.map[self.pos[0]])).index(0), list(reversed(self.map[self.pos[0]])).index(1))
			return self.pos[0], (len(self.map[self.pos[0]]) - 1) - tileYPos




class CubeMap(Map):
	def __init__(self, data, cubeSize = 50) -> None:
		self.map = {}
		self.pos = [0,0]
		self.facing = RIGHT
		self.cubeFace = 0

		face = 0
		for i in range(len(data) // cubeSize):
			for j in range(len(data[i * cubeSize]) // cubeSize):
				if data[i * cubeSize][j * cubeSize] == " ":
					continue
				newFace = []
				for x in range(cubeSize):
					faceRow = []
					for y in range(cubeSize):
						nx = (i * cubeSize) + x
						ny = (j * cubeSize) + y
						if data[nx][ny] == ".":
							faceRow.append(0)
						elif data[nx][ny] == "#":
							faceRow.append(1)
					newFace.append(faceRow)
				self.map[face] = newFace.copy()
				face += 1

		mapRow = data.pop(0)
		while mapRow != "":
			mapRow = data.pop(0)
		self.movement = re.findall('[0-9]+.?', data.pop(0))

		# for test
		#self.connections = {
		#	0:[5,3,2,1],
		#	1:[2,4,5,0],
		#	2:[3,4,1,0],
		#	3:[5,4,2,0],
		#	4:[5,1,2,3],
		#	5:[0,1,4,3]
		#}

		self.connections = {
			0:[1,2,3,5],
			1:[4,2,0,5],
			2:[1,4,3,0],
			3:[4,5,0,2],
			4:[1,5,3,2],
			5:[4,1,0,3]
		}


	def __str__(self) -> str:
		result = ""
		#for f in self.map:
		f = self.cubeFace
		mapStr = f"cube face {f}: \n"
		for x in range(len(self.map[f])):
			rowStr = ""
			for y in range(len(self.map[f][x])):
				if self.map[f][x][y] == 2:
					rowStr += " "
				elif [x, y] == self.pos and self.cubeFace == f:
					rowStr += ['R', 'D', 'L', 'U'][self.facing]
				elif self.map[f][x][y] == 1:
					rowStr += "#"
				elif self.map[f][x][y] == 0:
					rowStr += "."
			mapStr += rowStr + "\n"
		result += mapStr + "\n"
		return result

	def move(self):
		for move in self.movement:
			if move[-1] in ['L', 'R']:
				steps = int(move[:-1])
				dir = move[-1]
			else:
				steps = int(move)
				dir = None
			for i in range(steps):
				#print(self)
				#input()
				nx, ny = self.next_tile()
				if nx < 0 or ny < 0 or nx > len(self.map[self.cubeFace]) - 1 or ny > len(self.map[self.cubeFace][nx]) - 1:
					ox, oy, of, face = self.opposite_tile()
					print(self)
					print(self.cubeFace, self.pos, self.facing)
					print(of, ox, oy, face, self.map[of][ox][oy])
					if self.map[of][ox][oy] == 1:
						break
					else:
						self.pos = [ox, oy]
						self.cubeFace = of
						self.facing = face
					print(self)
					input()
				elif self.map[self.cubeFace][nx][ny] == 1:
					break
				else:
					self.pos = [nx, ny]
			self.turn(dir)

	def opposite_tile(self):
		nextFace = self.connections[self.cubeFace][self.facing]

		if self.connections[nextFace][self.facing] == self.cubeFace:

			#For test
			#if self.cubeFace in [1,4] and nextFace in [1,4]:
			#	return self.pos[0], abs((len(self.map[nextFace]) - 1) - self.pos[1]), nextFace, (self.facing + 2) % 4

			#For real
			if self.cubeFace in [0,3] and nextFace in [0,3]:
				return abs((len(self.map[nextFace]) - 1) - self.pos[0]), self.pos[1], nextFace, (self.facing + 2) % 4
			if self.cubeFace in [1, 4] and nextFace in [1, 4]:
				return abs((len(self.map[nextFace]) - 1) - self.pos[0]), self.pos[1], nextFace, (self.facing + 2) % 4

			return self.pos[0], self.pos[1], nextFace, (self.facing + 2) % 4

		elif self.connections[nextFace][(self.facing + 2) % 4] == self.cubeFace:

			#for real

			if self.facing in [UP,DOWN]:
				return abs((len(self.map[nextFace]) - 1) - self.pos[0]), self.pos[1], nextFace, self.facing

			elif self.facing in [RIGHT, LEFT]:
				return self.pos[0], abs((len(self.map[nextFace]) - 1) - self.pos[1]), nextFace, self.facing

		else:

			nextFacing = self.facing
			if self.connections[nextFace][(self.facing + 1) % 4] == self.cubeFace:
				nextFacing -= 1
				if nextFacing < 0:
					nextFacing = 3
			else:
				nextFacing += 1
				nextFacing %= 4


			#For test
			#if self.cubeFace in [2,0] and nextFace in [2,0]:
			#	return self.pos[1], self.pos[0], nextFace, (self.facing + 2) % 4

			#for real
			if self.cubeFace in [1,2] and nextFace in [1,2]:
				return self.pos[1], self.pos[0], nextFace,  nextFacing

			if self.cubeFace in [5,0] and nextFace in [5,0]:
				return self.pos[1], self.pos[0], nextFace, nextFacing


			if self.cubeFace in [5,4] and nextFace in [5,4]:
				return self.pos[1], self.pos[0], nextFace, nextFacing
			#if self.cubeFace == 5 and nextFace == 4:
			#	return self.pos[1],abs((len(self.map[nextFace]) - 1) - self.pos[0]), nextFace, nextFacing
			#elif self.cubeFace == 4 and nextFace == 5:
			#	return self.pos[1],self.pos[0], nextFace, nextFacing

			if self.cubeFace in [3,2] and nextFace in [3,2]:
				return self.pos[1],self.pos[0], nextFace, nextFacing

			return abs((len(self.map[nextFace]) - 1) - self.pos[1]), abs((len(self.map[nextFace]) - 1) - self.pos[0]), nextFace, nextFacing


def part1(data, test=False) -> str:
	map = Map(data)
	map.move()
	result = 1000 * (map.pos[0] + 1)
	result += 4 * (map.pos[1] + 1)
	result += map.facing
	return str(result)

def part2(data, test=False) -> str:
	cube = CubeMap(data, 50)
	try:
		cube.move()
	except Exception as e:
		print(e)
	facePos = [[2,0], [0,1], [1,1], [2,1], [3,2], [4,2]]

	result = 1000 * ((facePos[cube.cubeFace][1] * len(cube.map[0])) + cube.pos[0] + 1)
	result += 4 * ((facePos[cube.cubeFace][0] * len(cube.map[0])) + cube.pos[1] + 1)
	result += cube.facing
	return str(result)


# 34426
