import itertools
from intcode import IntcodeComputer


def part1(data, test=False) -> str:
    data = data[0].split(",")
    lastOutput = 0
    maxOutput = 0
    for pattern in itertools.permutations(range(5), 5):
        lastOutput = 0
        for i in pattern:
            comp = IntcodeComputer(data)
            comp.run(i)
            lastOutput = comp.run(lastOutput)
        maxOutput = max(maxOutput, lastOutput)

    return maxOutput


def part2(data, test=False) -> str:
    data = data[0].split(",")
    lastOutput = 0
    maxOutput = 0
    for pattern in itertools.permutations(range(5), 5):
        lastOutput = 0
        amps = []
        run = True
        patLen = len(pattern)
        for i in range(patLen):
            amps.append(IntcodeComputer(data))
            amps[i].run(pattern[i] + 5)
        while run:
            for i in range(patLen):
                lastOutput = amps[i].run(lastOutput)
            if amps[i].get_op_code() == "99":
                run = False
        maxOutput = max(maxOutput, lastOutput)
    return maxOutput
