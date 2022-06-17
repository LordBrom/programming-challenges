import math


def checkPowerSquare(powerLevels, x, y, size):
    powerSum = 0
    lowerRange = -math.floor(size / 2)
    upperRange = math.ceil(size / 2)
    for difX in range(lowerRange, upperRange):
        for difY in range(lowerRange, upperRange):
            checkX = x + difX
            checkY = y + difY
            if checkX < 0 or checkX >= len(powerLevels):
                return 0
            if checkY < 0 or checkY >= len(powerLevels[x]):
                return 0
            powerSum += powerLevels[checkX][checkY]
    return powerSum


def checkPowerLevels(powerLevels, allSizes=False):
    best = 0
    bestPos = None
    bestSize = None
    for x in range(len(powerLevels)):
        for y in range(len(powerLevels[x])):
            if not allSizes:
                check = checkPowerSquare(powerLevels, x, y, 3)
                if best < check:
                    best = check
                    bestPos = [x, y]
                    bestSize = 3
            else:
                for r in range(1, 301):
                    check = checkPowerSquare(powerLevels, x, y, r)
                    if best < check:
                        best = check
                        bestPos = [x, y]
                        bestSize = r

    bestPos[0] -= math.floor(bestSize / 2) - 1
    bestPos[1] -= math.floor(bestSize / 2) - 1
    return (bestPos, bestSize, best)


def calcPowerLevel(x, y, serial):
    rackID = x + 10
    result = ((rackID * y) + serial) * rackID
    if result < 100:
        result = 0
    else:
        result = int(str(result)[-3])
    return result - 5


def parseInput(data):
    powerLevels = []
    for x in range(1, 301):
        rowLevels = []
        for y in range(1, 301):
            rowLevels.append(calcPowerLevel(x, y, int(data)))
        powerLevels.append(rowLevels)
    return powerLevels


def part1(data, test=False) -> str:
    powerLevels = parseInput(data)
    largest = checkPowerLevels(powerLevels)
    return "{},{}".format(largest[0][0], largest[0][1])


def part2(data, test=False) -> str:
    powerLevels = parseInput(data)
    largest = checkPowerLevels(powerLevels, True)
    return "{},{},{}".format(largest[0][0], largest[0][1], largest[2])
