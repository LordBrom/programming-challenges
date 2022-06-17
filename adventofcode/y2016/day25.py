from y2016.monorailComputer import Computer


def part1(data, test=False) -> str:
    i = 0
    while True:
        comp = Computer(data, aVal=i)
        if comp.runInstructions():
            break
        i += 1
    return str(i)


def part2(data, test=False) -> str:
    return "Merry Christmas!"
