from typing import List
from y2019.intcode import IntcodeComputer


def appendInput(buildStr, newInput):
    for i in newInput:
        buildStr.append(ord(i))
    buildStr.append(ord("\n"))
    return buildStr


def part1(data, test=False) -> str:

    comp = IntcodeComputer(data[0].split(","))

    inputData: List[int] = []

    inputData = appendInput(inputData, "NOT C J")
    inputData = appendInput(inputData, "NOT B T")
    inputData = appendInput(inputData, "OR T J")
    inputData = appendInput(inputData, "NOT A T")
    inputData = appendInput(inputData, "OR T J")

    inputData = appendInput(inputData, "NOT D T")
    inputData = appendInput(inputData, "NOT J J")
    inputData = appendInput(inputData, "OR J T")
    inputData = appendInput(inputData, "NOT T J")

    inputData = appendInput(inputData, "WALK")

    result = []
    for i in inputData:
        result = comp.run(i, False)

    if test:
        outStr = ""
        for l in result:
            if l < 100000:
                outStr += chr(l)
        print(outStr)

    return str(result[-1])


def part2(data, test=False) -> str:

    comp = IntcodeComputer(data[0].split(","))

    inputData: List[str] = []

    inputData = appendInput(inputData, "NOT C J")
    inputData = appendInput(inputData, "NOT B T")
    inputData = appendInput(inputData, "OR T J")
    inputData = appendInput(inputData, "NOT A T")
    inputData = appendInput(inputData, "OR T J")

    inputData = appendInput(inputData, "NOT J J")

    inputData = appendInput(inputData, "NOT D T")
    inputData = appendInput(inputData, "OR T J")

    inputData = appendInput(inputData, "NOT E T")
    inputData = appendInput(inputData, "NOT T T")
    inputData = appendInput(inputData, "OR H T")
    inputData = appendInput(inputData, "NOT T T")
    inputData = appendInput(inputData, "OR T J")

    inputData = appendInput(inputData, "NOT J J")

    inputData = appendInput(inputData, "RUN")

    result = []
    for i in inputData:
        result = comp.run(i, False)

    return str(result[-1])
