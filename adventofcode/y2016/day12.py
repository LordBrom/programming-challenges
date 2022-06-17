from monorailComputer import Computer


def part1(data, test=False) -> str:
    comp = Computer(data)
    comp.runInstructions()
    return comp.registers["a"]


def part2(data, test=False) -> str:
    comp = Computer(data, cVal=1)
    comp.runInstructions()
    return comp.registers["a"]
