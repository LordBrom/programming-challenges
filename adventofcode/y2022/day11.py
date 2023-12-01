import math

class Monkey():
	def __init__(self, num, items, op, test, true, false, div = None) -> None:
		self.num = num
		self.items = items
		self.op = op
		self.test = int(test)
		self.true = true
		self.false = false
		self.itemsChecked = 0
		self.div = div

	def __str__(self) -> str:
		return f"Monkey {self.num}: holding {str(self.items)}"

	def take_turn(self, monkeys):
		while len(self.items):
			self.itemsChecked += 1
			worryLevel = int(self.items.pop(0))
			opSplit = self.op.split(" ")
			if opSplit[0] == "+":
				if opSplit[1] == "old":
					worryLevel += worryLevel
				else:
					worryLevel += int(opSplit[1])
			else:
				if opSplit[1] == "old":
					worryLevel *= worryLevel
				else:
					worryLevel *= int(opSplit[1])

			if self.div == None:
				worryLevel = math.floor(worryLevel / 3)
			else:
				worryLevel %= self.div

			if worryLevel % self.test == 0:
				monkeys[self.true].items.append(worryLevel)
			else:
				monkeys[self.false].items.append(worryLevel)

def parse_monkeys(data):
	monkeys = {}
	while len(data) > 0:
		num = data.pop(0)[7:-1]
		items = data.pop(0)[18:].split(", ")
		op = data.pop(0)[23:]
		test = data.pop(0)[21:]
		true = data.pop(0)[29:]
		false = data.pop(0)[30:]
		if len(data) > 0:
			data.pop(0)

		monkeys[num] = Monkey(num, items, op, test, true, false)
	return monkeys

def part1(data, test=False) -> str:
	monkeys = parse_monkeys(data)
	for i in range(20):
		for m in monkeys:
			monkeys[m].take_turn(monkeys)

	results = [monkeys[m].itemsChecked for m in monkeys]
	results.sort()

	return str(results[-1] * results[-2])


def part2(data, test=False) -> str:
	monkeys = parse_monkeys(data)

	lcm = 1
	for x in [monkeys[m].test for m in monkeys]:
		lcm *= lcm * x

	for m in monkeys:
		monkeys[m].div = lcm

	for i in range(10000):
		for m in monkeys:
			monkeys[m].take_turn(monkeys)

	results = [monkeys[m].itemsChecked for m in monkeys]
	results.sort()

	return str(results[-1] * results[-2])
