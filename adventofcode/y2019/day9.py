from intcode import IntcodeComputer


def part1(data, test=False) -> str:
    comp = IntcodeComputer(data[0].split(","))
    return comp.run(1)


def part2(data, test=False) -> str:
    comp = IntcodeComputer(data[0].split(","))
    return comp.run(2)
