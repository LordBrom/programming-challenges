import re


class ManualPaper:
    def __init__(self) -> None:
        self.paper = [[20151125]]

    def getCodeAtPos(self, x, y):
        while len(self.paper) <= x:
            self.paper.append([])
        while len(self.paper[x]) <= y:
            self.paper[x].append(None)

        if self.paper[x][y] == None:
            prevX, prevY = self.getPreviousPos(x, y)
            prevVal = self.getCodeAtPos(prevX, prevY)

            self.paper[x][y] = self.nextCode(prevVal)

        return self.paper[x][y]

    def getPreviousPos(self, x, y):
        if x == 0 and y == 0:
            return None, None
        if x == 0:
            return y - 1, 0
        return x - 1, y + 1

    def getNextPos(self, x, y):
        if y == 0:
            return 0, x + 1
        return x + 1, y - 1

    def nextCode(self, val):
        nextNum = val * 252533
        return nextNum % 33554393


def parseInput(data):
    reResult = re.search(
        "To continue, please consult the code grid in the manual.  Enter the code at row ([0-9]+), column ([0-9]+).",
        data,
    )
    return int(reResult.group(1)), int(reResult.group(2))


def part1(data, test=False) -> str:
    data = data[0]
    col, row = parseInput(data)
    manualPaper = ManualPaper()
    x = 0
    y = 0
    while x <= row or y <= col:
        manualPaper.getCodeAtPos(x, y)
        x, y = manualPaper.getNextPos(x, y)
    return str(manualPaper.getCodeAtPos(row - 1, col - 1))


def part2(data, test=False) -> str:
    return "Merry Christmas!!!"
