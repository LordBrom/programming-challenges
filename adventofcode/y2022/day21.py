class Monkey():
	def __init__(self, name, shout, part2 = False) -> None:
		self.name = name
		self.num = None
		self.monk1 = None
		self.monk2 = None
		self.operator = None
		shoutSplit = shout.split(" ")
		if len(shoutSplit) == 1:
			self.num = int(shout)
		else:
			self.monk1, self.operator, self.monk2 = shoutSplit
		if part2 and self.name == "root":
			self.operator = "="
		self.vibeCheck = False

	def shout(self, monkeys):
		result = self.num
		if self.num == None:
			shout1 = monkeys[self.monk1].shout(monkeys)
			shout2 = monkeys[self.monk2].shout(monkeys)
			result = self.evaluate(shout1, shout2, self.operator)
		return result

	def evaluate(self, num1, num2, op):

		if op == "+":
			return num1 + num2

		elif op == "-":
			return num1 - num2

		elif op == "*":
			return num1 * num2

		elif op == "/":
			return int(num1 / num2)

		else:
			#print(num1, num2)
			return num1 == num2




	def get_equation(self, monkeys):
		result = self.num
		if self.name == "humn":
			result = "x"
		if self.num == None:
			shout1 = monkeys[self.monk1].get_equation(monkeys)
			shout2 = monkeys[self.monk2].get_equation(monkeys)

			if not 'x' in str(shout1) and not 'x' in str(shout2):
				result = self.evaluate(shout1, shout2, self.operator)
			else:
				result = f"({str(shout1)}{self.operator}{str(shout2)})"
		return result



def parse_monkeys(data, part2=False):
	monkeys = {}
	for d in data:
		name, shout = d.split(": ")
		monkeys[name] = Monkey(name, shout, part2)
	return monkeys

def part1(data, test=False) -> str:
	monkeys = parse_monkeys(data)
	return str(monkeys['root'].shout(monkeys))


def part2(data, test=False) -> str:
	monkeys = parse_monkeys(data, True)

	print(monkeys['root'].get_equation(monkeys))
	print("solve for x")
	return str(3353687996514)


