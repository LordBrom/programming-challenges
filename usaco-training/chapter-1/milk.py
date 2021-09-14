"""
ID: mills.n2
LANG: PYTHON3
TASK: milk
"""


class Farmer:
	def __init__(self, milkCost, milkStock):
		self.milkCost = milkCost
		self.milkStock = milkStock

	def sell_milk(self, amount):
		if amount > self.milkStock:
			soldCost = self.milkStock * self.milkCost
			soldStock = self.milkStock
			self.milkStock = 0
			return [soldCost, soldStock]
		self.milkStock -= amount
		return [amount * self.milkCost, amount]

inFile = open("milk.in", "r").read().split("\n")
inFile.pop()
outFile = open("milk.out", "w")

firstLine = inFile.pop(0).split(" ")
milkNeeded = int(firstLine[0])
farmersAvailable = int(firstLine[1])

milkCost = 0
farmers = []

for l in inFile:
	lineSplit = l.split(" ")
	farmers.append(Farmer(int(lineSplit[0]), int(lineSplit[1])))

farmers.sort(key=lambda x: x.milkCost)

for f in farmers:
	p = f.sell_milk(milkNeeded)
	milkCost += p[0]
	milkNeeded -= p[1]
	if milkNeeded == 0:
		break

outFile.write(str(milkCost) + '\n')
outFile.close()
