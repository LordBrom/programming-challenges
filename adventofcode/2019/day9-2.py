
from intcode import IntcodeComputer

inFile = open("inputs/day9.in", "r").read().split(",")

comp = IntcodeComputer(inFile)
print(comp.run(2))
