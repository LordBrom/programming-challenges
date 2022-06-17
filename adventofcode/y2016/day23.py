from monorailComputer import Computer


def part1(data):
    comp = Computer(data, aVal=7)
    comp.runInstructions()
    return comp.registers['a']


def part2(data):
    n = 12
    for i in range(1, 12):
        n *= i
    return n + (84 * 89)
