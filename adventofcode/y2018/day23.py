import sys
import re


class NanoBot:
    def __init__(self, inData) -> None:
        reStr = "pos=<([-0-9]+),([-0-9]+),([-0-9]+)>, r=([-0-9]+)"
        reResult = re.search(reStr, inData)
        self.x = int(reResult.group(1))
        self.y = int(reResult.group(2))
        self.z = int(reResult.group(3))
        self.r = int(reResult.group(4))

    def __str__(self) -> str:
        return "pos=<{},{},{}>, r={}".format(self.x, self.y, self.z, self.r)

    def posArray(self):
        return [self.x, self.y, self.z]

    def inRange(self, posArray):
        return manhattanDistance(self.posArray(), posArray) <= self.r


def manhattanDistance(point1, point2):
    diffX = abs(point1[0] - point2[0])
    diffY = abs(point1[1] - point2[1])
    diffZ = abs(point1[2] - point2[2])
    return diffX + diffY + diffZ


def parseInput(data):
    nanoBots = []
    strongest = None
    for d in data:
        newBot = NanoBot(d)
        if strongest == None or newBot.r > strongest.r:
            strongest = newBot
        nanoBots.append(newBot)
    return nanoBots, strongest


def part1(data, test=False) -> str:
    nanoBots, strongest = parseInput(data)

    result = 0
    for bot in nanoBots:
        if strongest.inRange(bot.posArray()):
            result += 1

    return str(result)


def part2(data, test=False) -> str:
    nanoBots = parseInput(data)[0]
    best = 0
    bestPos = [0, 0, 0]

    xMax = 0
    xMin = sys.maxsize
    yMax = 0
    yMin = sys.maxsize
    zMax = 0
    zMin = sys.maxsize

    for bot in nanoBots:
        xMax = max(xMax, bot.x)
        xMin = min(xMin, bot.x)
        yMax = max(yMax, bot.y)
        yMin = min(yMin, bot.y)
        zMax = max(zMax, bot.z)
        zMin = min(zMin, bot.z)

    xRange = [xMin, xMax + 1]
    yRange = [yMin, yMax + 1]
    zRange = [zMin, zMax + 1]

    for x in range(xRange[0], xRange[1]):
        for y in range(yRange[0], yRange[1]):
            for z in range(zRange[0], zRange[1]):
                checkPos = [x, y, z]
                check = 0
                for bot in nanoBots:
                    if bot.inRange(checkPos):
                        check += 1
                if check > best:
                    best = check
                    bestPos = checkPos
    return manhattanDistance([0, 0, 0], bestPos)


# 10383357 - low
# 167596085 - high
