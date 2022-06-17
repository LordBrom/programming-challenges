from y2019.intcode import IntcodeComputer


def part1(data, test=False) -> str:
    inFile = data[0].split(",")

    inFile[1] = 12
    inFile[2] = 2

    comp = IntcodeComputer(inFile)
    comp.run()

    return comp.get_intcode()[0]


def part2(data, test=False) -> str:
    inFile = data[0].split(",")
    for i in range(100):
        for j in range(100):
            inFile[1] = i
            inFile[2] = j

            comp = IntcodeComputer(inFile.copy())
            comp.run()
            check = comp.get_intcode()[0]

            if check == 19690720:
                return str(100 * i + j)
    return "..."
