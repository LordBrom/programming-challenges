"""
ID: mills.n2
LANG: PYTHON3
TASK: beads
"""

class Necklace:
	def __init__(self, beads):
		self.beads = beads
		self.oneColor = False
		if self.beads.find('r') == -1 or self.beads.find('b') == -1:
			self.oneColor = True
		else:
			self.color_white_beads()
			self.rotate()

	def next_bead_pos(self, pos):
		if pos + 1 >= len(self.beads):
			return 0
		return pos + 1

	def prev_bead_pos(self, pos):
		if pos - 1 == 0:
			return len(self.beads) - 1
		return pos - 1

	def next_non_white_bead_pos(self, pos):
		index = self.next_bead_pos(pos)
		while index != pos:
			if (self.beads[index] != 'w'):
				return index
			index = self.next_bead_pos(index)
		return -1

	def prev_non_white_bead_pos(self, pos):
		index = self.prev_bead_pos(pos)
		while index != pos:
			if (self.beads[index] != 'w'):
				return index
			index = self.prev_bead_pos(index)
		return -1

	def next_diff_color_bead_pos(self, pos):
		color = self.beads[pos]
		index = self.next_bead_pos(pos)
		while index != pos:
			if (self.beads[index] != color):
				return index
			index = self.next_bead_pos(index)
		return -1

	def color_white_beads(self):
		wPos = self.beads.find('w', 0)
		while wPos != -1:
			leftColor = self.beads[self.prev_non_white_bead_pos(wPos)]
			rightColor = self.beads[self.next_non_white_bead_pos(wPos)]

			if leftColor == rightColor:
				self.beads = self.beads[0:wPos] + leftColor + self.beads[wPos+1:]
			wPos = self.beads.find('w', wPos + 1)

	def rotate(self):
		firstIndex = self.next_non_white_bead_pos(-1)
		index = self.next_diff_color_bead_pos(firstIndex)
		while self.beads[index] == 'w':
			index = self.next_diff_color_bead_pos(index)
		self.beads = self.beads[index:] + self.beads[0:index]

	def count_beads_from_pos(self, startPos):
		result = 0
		nonWhiteCount = 0
		nextPos = startPos
		while nonWhiteCount < 2:
			color = self.beads[nextPos]
			lastPos = nextPos
			nextPos = self.next_diff_color_bead_pos(lastPos)
			if color != 'w':
				nonWhiteCount += 1
			if (nextPos < lastPos):
				result += len(self.beads) - lastPos
			else:
				result += abs(nextPos - lastPos)

		if (self.beads[nextPos] == 'w'):
			lastPos = nextPos
			nextPos = self.next_diff_color_bead_pos(lastPos)
			if (nextPos < lastPos):
				result += len(self.beads) - lastPos
			else:
				result += abs(nextPos - lastPos)

		return result

	def count_beads(self):
		index = 0
		result = 0
		if self.oneColor:
			return len(self.beads)
		while 1:
			result = max(result, self.count_beads_from_pos(index))
			nextIndex = self.next_diff_color_bead_pos(index)
			if nextIndex < index:
				break
			index = nextIndex

		return min(result, len(self.beads))

inFile = open("beads.in", "r").read().split("\n")
inFile.pop()
outFile = open("beads.out", "w")
beadCount = int(inFile[0])

necklace = Necklace(inFile[1])

outFile.write(str(necklace.count_beads()) + "\n")
outFile.close()
