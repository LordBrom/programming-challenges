import re


class LightGrid:
    def __init__(self, part1=True, gridSize=1000) -> None:
        self.part1 = part1
        if self.part1:
            self.grid = [[False for x in range(gridSize)] for y in range(gridSize)]
        else:
            self.grid = [[0 for x in range(gridSize)] for y in range(gridSize)]

    def doInstruction(self, inLine):
        reStr = "(turn on|toggle|turn off) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)"
        reResult = re.search(reStr, inLine)
        action = reResult.group(1)
        x1 = int(reResult.group(2))
        y1 = int(reResult.group(3))
        x2 = int(reResult.group(4))
        y2 = int(reResult.group(5))
        if action == "turn on":
            self.setRange(x1, y1, x2, y2)
        elif action == "turn off":
            self.setRange(x1, y1, x2, y2, False)
        else:
            self.toggleRange(x1, y1, x2, y2)

    def setRange(self, x1, y1, x2, y2, setTo=True):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if self.part1:
                    self.grid[x][y] = setTo
                elif setTo:
                    self.grid[x][y] += 1
                else:
                    self.grid[x][y] = max(0, self.grid[x][y] - 1)

    def toggleRange(self, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if self.part1:
                    self.grid[x][y] = not self.grid[x][y]
                else:
                    self.grid[x][y] += 2

    def countOn(self):
        result = 0
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                if self.grid[x][y]:
                    if self.part1:
                        result += 1
                    else:
                        result += self.grid[x][y]
        return result


def part1(data, test=False) -> str:
    lightGrid = LightGrid()
    for d in data:
        lightGrid.doInstruction(d)
    return str(lightGrid.countOn())


def part2(data, test=False) -> str:
    lightGrid = LightGrid(False)
    for d in data:
        lightGrid.doInstruction(d)
    return str(lightGrid.countOn())
