class CPU():

	def __init__(self, steps, startCheck = 20) -> None:
		self.steps = steps
		self.cycle = 0
		self.register = 1
		self.result = 0
		self.check = startCheck
		self.CRT = [""]
		self.crtPos = 0

	def __str__(self) -> str:
		return '\n'.join(self.CRT)

	def run(self):
		for d in self.steps:
			if d == "noop":
				self.step()
				continue
			dSplit = d.split(" ")
			self.step()
			self.step()

			self.register += int(dSplit[1])

	def step(self):
		self.add_pixel()
		self.cycle += 1
		self.crtPos += 1
		if self.cycle >= self.check:
			self.result += self.check * self.register
			self.check += 40
			self.CRT.append("")
			self.crtPos = 0

	def add_pixel(self):
		if self.crtPos in list(range(self.register - 1, self.register + 2)):
			self.CRT[-1] += "#"
		else:
			self.CRT[-1] += "."

def part1(data, test=False) -> str:
	cpu = CPU(data)
	cpu.run()
	return str(cpu.result)


def part2(data, test=False) -> str:
	cpu = CPU(data, 40)
	cpu.run()
	print(cpu)
	return "see above"
