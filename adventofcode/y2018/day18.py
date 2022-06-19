from typing import List

class Acre:
    def __init__(self, start) -> None:
        self.state = start
        self.nextState = None
        self.adjacent: List[Acre] = []

    def __str__(self) -> str:
        return self.state

    def __eq__(self, __o: object) -> bool:
        return self.state == __o

    def updateState(self):
        if self.state == ".":
            treeCount = 0
            for a in self.adjacent:
                if a == "|":
                    treeCount += 1
                    if treeCount >= 3:
                        self.nextState = "|"
                        return
                self.nextState = "."

        elif self.state == "|":
            lumberyardCount = 0
            for a in self.adjacent:
                if a == "#":
                    lumberyardCount += 1
                    if lumberyardCount >= 3:
                        self.nextState = "#"
                        return
            self.nextState = "|"

        else:  # '#'
            treeCount = 0
            lumberyardCount = 0
            for a in self.adjacent:
                if a == "|":
                    treeCount += 1
                elif a == "#":
                    lumberyardCount += 1
                if lumberyardCount >= 1 and treeCount >= 1:
                    self.nextState = "#"
                    return
            self.nextState = "."


class LumberArea:
    def __init__(self, area) -> None:
        self.area = []

        for i in area:
            row = []
            for j in i:
                row.append(Acre(j))
            self.area.append(row)

        for x in range(len(self.area)):
            for y in range(len(self.area[x])):
                adjacent = self.getAdjacent(x, y)
                for a in adjacent:
                    self.area[x][y].adjacent.append(self.area[a[0]][a[1]])

    def __str__(self) -> str:
        result = ""
        for r in self.area:
            rowStr = ""
            for a in r:
                rowStr += str(a)
            result += "\n" + rowStr
        return result

    def minutePass(self):
        for r in self.area:
            for a in r:
                a.updateState()

        for r in self.area:
            for a in r:
                a.state = a.nextState

    def getAdjacent(self, x, y):
        result = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                diffX = x + dx
                diffY = y + dy
                if diffX < 0 or diffX >= len(self.area):
                    continue
                if diffY < 0 or diffY >= len(self.area[0]):
                    continue
                result.append([diffX, diffY])
        return result

    def result(self):
        woodedAcres = 0
        lumberYards = 0
        for x in range(len(self.area)):
            for y in range(len(self.area[x])):
                if self.area[x][y] == "|":
                    woodedAcres += 1
                elif self.area[x][y] == "#":
                    lumberYards += 1
        return woodedAcres * lumberYards


def part1(data, test=False) -> str:
    lumberArea = LumberArea(data)
    for t in range(10):
        lumberArea.minutePass()

    return str(lumberArea.result())


def part2(data, test=False) -> str:
    lumberArea = LumberArea(data)
    for t in range(1000000000):
        lumberArea.minutePass()

    return str(lumberArea.result())
