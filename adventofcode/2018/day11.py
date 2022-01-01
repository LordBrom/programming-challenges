

def checkPowerLevels(powerLevels):
    best = 0
    bestPos = None
    bestSize = None
    for x in range(len(powerLevels)):
        for y in range(len(powerLevels[x])):
            powerSum = 0
            for difX in range(-1, 2):
                for difY in range(-1, 2):
                    checkX = x + difX
                    checkY = y + difY
                    if checkX < 0 or checkX >= len(powerLevels):
                        continue
                    if checkY < 0 or checkY >= len(powerLevels[x]):
                        continue
                    powerSum += powerLevels[checkX][checkY]
            if best < powerSum:
                best = powerSum
                bestPos = [x, y]
    return (bestPos, best, bestSize)


def calcPowerLevel(x, y, serial):
    rackID = x + 10
    result = ((rackID * y) + serial) * rackID
    if result < 100:
        result = 0
    else:
        result = int(str(result)[-3])
    return result - 5


def part1(data):
    powerLevels = []
    for x in range(1, 301):
        rowLevels = []
        for y in range(1, 301):
            rowLevels.append(calcPowerLevel(x, y, int(data)))
        powerLevels.append(rowLevels)

    largestPos = checkPowerLevels(powerLevels)[0]

    return str(largestPos[0]) + "," + str(largestPos[1])


def part2(data):
    return "not implemented"
