import sys
import re
from typing import List

# default: 1000
sys.setrecursionlimit(3000)


class SandPit:
    def __init__(self, clayVeins) -> None:
        maxX = 0
        minX = sys.maxsize
        maxY = 0
        minY = sys.maxsize

        for vein in clayVeins:
            if vein[0] == "y":
                maxX = max(maxX, int(vein[1]))
                minX = min(minX, int(vein[1]))
                maxY = max(maxY, int(vein[4]))
                minY = min(minY, int(vein[3]))
            else:
                maxY = max(maxY, int(vein[1]))
                minY = min(minY, int(vein[1]))
                maxX = max(maxX, int(vein[4]))
                minX = min(minX, int(vein[3]))

        pitSizeX = (maxX - minX) + 2
        pitSizeY = (maxY - minY) + 3
        self.pitOffsetX = minX - 1
        self.pitOffsetY = minY - 1

        self.pit = [["." for y in range(pitSizeY)] for x in range(pitSizeX)]
        for vein in clayVeins:
            for i in range(int(vein[3]), int(vein[4]) + 1):
                if vein[0] == "y":
                    self.pit[int(vein[1]) - self.pitOffsetX][i - self.pitOffsetY] = "#"
                else:
                    self.pit[i - self.pitOffsetX][int(vein[1]) - self.pitOffsetY] = "#"

        self.water: List[List[int]] = []
        self.debug = False

    def __str__(self) -> str:
        result = ""
        for x in range(len(self.pit)):
            result += "\n"
            for y in range(len(self.pit[x])):
                if x == 0 and y + self.pitOffsetY == 500:
                    result += "+"
                else:
                    result += self.pit[x][y]
        return result

    def spreadWater(self, x, y):
        print(self)
        input()
        if x + 1 >= len(self.pit):
            self.pit[x][y] = "|"
            return True

        if self.pit[x + 1][y] == ".":
            self.pit[x + 1][y] = "~"
            self.water.append([x + 1, y])
            if self.spreadWater(x + 1, y):
                self.pit[x][y] = "|"
                return True
        elif self.pit[x + 1][y] == "|":
            self.pit[x][y] = "|"
            return True

        spread = False

        # Check Right
        if y + 1 < len(self.pit[0]) and self.pit[x][y + 1] in ["."]:
            self.pit[x][y + 1] = "~"
            self.water.append([x, y + 1])
            if self.spreadWater(x, y + 1):
                self.pit[x][y] = "|"
                spread = True
        if y + 1 < len(self.pit[0]) and self.pit[x][y + 1] == "|":
            self.pit[x][y] = "|"
            spread = True

        # Check Left
        if y - 1 >= 0 and self.pit[x][y - 1] in ["."]:
            self.pit[x][y - 1] = "~"
            self.water.append([x, y - 1])
            if self.spreadWater(x, y - 1):
                self.pit[x][y] = "|"
                spread = True
        if y - 1 >= 0 and self.pit[x][y - 1] == "|":
            self.pit[x][y] = "|"
            spread = True

        # Re-Check Right (to set correct char incase left makes it)
        if y + 1 < len(self.pit[0]) and self.pit[x][y + 1] in ["~"]:
            if self.spreadWater(x, y + 1):
                self.pit[x][y] = "|"
                spread = True

        return spread


def parseInput(data):
    result = []
    reStr = "(x|y)=([0-9]+), (x|y)=([0-9]+)\.\.([0-9]+)"
    for d in data:
        reResult = re.search(reStr, d)
        result.append(list(reResult.groups()))
    return result


def part1(data, test=False) -> str:
    sandPit = SandPit(parseInput(data))
    sandPit.spreadWater(0, 500 - sandPit.pitOffsetY)
    return str(len(sandPit.water))


def part2(data, test=False) -> str:
    sandPit = SandPit(parseInput(data))
    sandPit.spreadWater(0, 500 - sandPit.pitOffsetY)
    result = 0
    for w in sandPit.water:
        if sandPit.pit[w[0]][w[1]] == "~":
            result += 1
    str(sandPit)
    return str(result)
