from intcode import IntcodeComputer

inFile = open("inputs/day5.in", "r").read().split(",")
comp = IntcodeComputer(inFile)
print(comp.run(1))
