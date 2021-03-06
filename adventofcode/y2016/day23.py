from y2016.monorailComputer import Computer


def part1(data, test=False) -> str:
    comp = Computer(data, aVal=7)
    comp.runInstructions()
    return str(comp.registers["a"])


def part2(data, test=False) -> str:
    n = 12
    for i in range(1, 12):
        n *= i
    return str(n + (84 * 89))
