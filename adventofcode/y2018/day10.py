import sys
import re


class StarPoint:
    def __init__(self, position, velocity) -> None:
        self.position = [position[1], position[0]]
        self.velocity = [velocity[1], velocity[0]]

    def __str__(self) -> str:
        return "position=<{}, {}> velocity=<{}, {}>".format(
            self.position[0], self.position[1], self.velocity[0], self.velocity[1]
        )

    def moveTick(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]


def parseInput(data):
    result = []
    reStr = "position=<([-0-9, ]+)> velocity=<([-0-9, ]+)>"
    for d in data:
        reResult = re.search(reStr, d)
        position = parseHelper(reResult.group(1))
        velocity = parseHelper(reResult.group(2))
        result.append(StarPoint(position, velocity))
    return result


def parseHelper(inStr):
    strSpit = inStr.split(",")
    return int(strSpit[0].strip()), int(strSpit[1].strip())


def printStarPoints(starPoints, doPrint=True):
    positions = [x.position for x in starPoints]
    minX = sys.maxsize
    maxX = -sys.maxsize
    minY = sys.maxsize
    maxY = -sys.maxsize
    for sp in positions:
        minX = min(minX, sp[0])
        maxX = max(maxX, sp[0])
        minY = min(minY, sp[1])
        maxY = max(maxY, sp[1])

    if maxX - minX <= 10:  # 7 for example
        if doPrint:
            for x in range(minX, maxX + 1):
                outStr = ""
                for y in range(minY, maxY + 1):
                    if [x, y] in positions:
                        outStr += "#"
                    else:
                        outStr += "."
                print(outStr)
        return True
    return False


def part1(data, test=False) -> str:
    starPoints = parseInput(data)
    while not printStarPoints(starPoints):
        for sp in starPoints:
            sp.moveTick()
    return "see above"


def part2(data, test=False) -> str:
    starPoints = parseInput(data)
    steps = 0
    while not printStarPoints(starPoints, False):
        steps += 1
        for sp in starPoints:
            sp.moveTick()
    return steps
