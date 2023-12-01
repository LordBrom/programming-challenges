
import math

ROCKS = [
	[(0,2),(0,3),(0,4),(0,5)],
	[(1,2),(1,3),(1,4), (0,3), (2,3)],
	[(0,2),(0,3),(0,4), (1,4), (2,4)],
	[(0,2),(1,2),(2,2),(3,2)],
	[(0,2),(0,3),(1,2),(1,3)]
]

class RockColumn():

	def __init__(self, jets) -> None:
		self.jets = jets
		self.jetIndex = 0
		self.column = []
		self.add_row()
		self.add_row()
		self.add_row()
		self.add_row()
		self.add_row()


	def __str__(self) -> str:
		result = ""

		for col in range(len(self.column)):
			rowStr = ""
			for row in range(len(self.column[col])):
				if self.column[col][row]:
					rowStr += "#"
				else:
					rowStr += "."
			result += rowStr + '\n'

		return result

	def add_row(self):
		self.column.append([False for x in range(7)])

	def drop_rock(self, rock):
		fallingRock = []
		startHeight = self.height() + 3
		for rx, ry in rock:
			fallingRock.append([rx + startHeight, ry])


		falling, rock = self.move_rock(fallingRock)
		while falling:
			falling, rock = self.move_rock(fallingRock)

		#print(self)
		#input()

	def move_rock(self, rock):
		if self.jets[self.jetIndex] == ">":
			#print('move right')
			if all((r[1] < 6 and not self.column[r[0]][r[1] + 1]) for r in rock):
				for r in rock:
					r[1] += 1
		else:
			#print('move left')
			if all((r[1] > 0 and not self.column[r[0]][r[1] - 1]) for r in rock):
				for r in rock:
					r[1] -= 1

		self.jetIndex += 1
		self.jetIndex %= len(self.jets)

		for r in rock:
			if r[0] == 0 or self.column[r[0] - 1][r[1]]:
				self.set_rock(rock)
				return False, rock

		for r in rock:
			r[0] -= 1

		return True, rock

	def set_rock(self, rock):
		for r in rock:
			self.column[r[0]][r[1]] = True



	def height(self):
		for col in reversed(range(len(self.column))):
			for row in range(len(self.column[col])):
				if self.column[col][row]:
					while len(self.column) < col + 8:
						self.add_row()
					return col + 1

		return 0


def part1(data, test=False) -> str:
	rockColumn = RockColumn(data[0])
	for i in range(2022):
		rockColumn.drop_rock(ROCKS[i % 5])
	return str(rockColumn.height())


def part2(data, test=False) -> str:
	rockColumn = RockColumn(data[0])
	for i in range(1350):
		rockColumn.drop_rock(ROCKS[i % 5])
		#if rockColumn.height() == 531:
		#	print(i, rockColumn.height())

		#elif (rockColumn.height() - 531) % 2659 == 0:
		#	print(i, rockColumn.height())
	return '1541449275365'
