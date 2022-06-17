from y2019.intcode import IntcodeComputer
import math


def getPoint(data, x, y):
    comp = IntcodeComputer(data)
    comp.run(x)
    return comp.run(y)


def getScanRow(data, row, printRow=False, offset=0):
    scanStart = False
    index = 0
    scanning = None
    scanRange = [None, None]
    scanRow = []
    outStr = str(row) + " "
    while not scanStart or scanning == 1:
        scanning = getPoint(data, row, index)
        if not scanStart and scanning == 1:
            scanRow.append(True)
            outStr += "#"
            scanRange[0] = index
            scanStart = True
        elif scanStart and scanning == 0:
            outStr += "."
            scanRange[1] = index
            break
        elif scanStart:
            scanRow.append(True)
            outStr += "#"
        elif index >= offset:
            scanRow.append(False)
            outStr += "."
        index += 1
    if printRow:
        print(outStr + " " + str(scanRange[1] - scanRange[0]))

    return scanRow, scanRange


def part1(data, test=False) -> str:
    data = data.split(",")
    scan = 50
    result = 0
    for x in range(scan):
        for y in range(scan):
            result += getPoint(data, x, y)
    return str(result)


def part2(data, test=False) -> str:
    row1000 = getScanRow(data.split(","), 1000)

    m2 = 1000 / row1000[1][0]
    m1 = 1000 / row1000[1][1]

    x2 = ((m1 * 99) + 99) / (m2 - m1)
    y1 = m2 * x2 - 99

    x2 = math.ceil(x2)
    y1 = math.ceil(y1)

    return (x2 * 10000) + y1


# not 8651326 :/
