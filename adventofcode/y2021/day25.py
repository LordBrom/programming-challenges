class Trench:
    def __init__(self, data) -> None:
        self.trench = []
        for d in data:
            row = []
            for s in d:
                if s == "v":
                    row.append(1)
                elif s == ">":
                    row.append(2)
                else:
                    row.append(0)
            self.trench.append(row)

    def __str__(self) -> str:
        result = "-------------"
        for x in range(len(self.trench)):
            rowStr = "\n"
            for y in range(len(self.trench[x])):
                if self.trench[x][y] == 0:
                    rowStr += "."
                elif self.trench[x][y] == 1:
                    rowStr += "v"
                elif self.trench[x][y] == 2:
                    rowStr += ">"
            result += rowStr
        result += "\n-------------"

        return result

    def moveCucumbers(self, moveEast=True):
        startTrench = self.trench.copy()
        newTrench = []
        for x in range(len(self.trench)):
            newTrench.append([0 for i in range(len(self.trench[x]))])

        for x in range(len(self.trench)):
            for y in range(len(self.trench[x])):
                if self.trench[x][y] == 0:
                    continue
                elif (moveEast and self.trench[x][y] == 1) or (
                    not moveEast and self.trench[x][y] == 2
                ):
                    newTrench[x][y] = self.trench[x][y]
                else:
                    nextX, nextY = self.nextSpot([x, y])
                    if self.trench[nextX][nextY] == 0:
                        newTrench[x][y] = 0
                        newTrench[nextX][nextY] = self.trench[x][y]
                    else:
                        newTrench[x][y] = self.trench[x][y]

        self.trench = newTrench
        if moveEast:
            return self.moveCucumbers(False) and startTrench == self.trench
        return startTrench == self.trench

    def nextSpot(self, pos):
        if self.trench[pos[0]][pos[1]] == 1:
            pos[0] += 1
            pos[0] %= len(self.trench)
        else:
            pos[1] += 1
            pos[1] %= len(self.trench[0])
        return pos[0], pos[1]


def part1(data, test=False) -> str:
    trench = Trench(data)
    found = False
    result = 0
    while not found:
        found = trench.moveCucumbers()
        result += 1

    return str(result)


def part2(data, test=False) -> str:
    return "Merry Christmas!!!"
