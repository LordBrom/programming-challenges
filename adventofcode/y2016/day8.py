import re


class Screen:
    def __init__(self, screenWidth=50, screenHeight=6) -> None:
        self.pixels = [[False for x in range(screenWidth)] for y in range(screenHeight)]

    def __str__(self) -> str:
        result = "=================================================="
        for row in self.pixels:
            rowStr = ""
            for pixel in row:
                if pixel:
                    rowStr += "#"
                else:
                    rowStr += " "
            result += "\n" + rowStr
        result += "\n=================================================="
        return result

    def addRect(self, width, height):
        for x in range(height):
            for y in range(width):
                self.pixels[x][y] = True
        pass

    def rotateRow(self, row, count=1):
        for c in range(count):
            pixelHolder = self.pixels[row][-1]
            for i in reversed(range(len(self.pixels[row]) - 1)):
                self.pixels[row][i + 1] = self.pixels[row][i]
            self.pixels[row][0] = pixelHolder

    def rotateCol(self, col, count=1):
        for c in range(count):
            pixelHolder = self.pixels[-1][col]
            for i in reversed(range(len(self.pixels) - 1)):
                self.pixels[i + 1][col] = self.pixels[i][col]
            self.pixels[0][col] = pixelHolder

    def countPixels(self):
        result = 0
        for row in self.pixels:
            for pixel in row:
                if pixel:
                    result += 1
        return result


def part1(data, test=False) -> str:
    reStr = "(?:(rect) |rotate (column|row) )(?:([0-9]+)x([0-9]+)|(?:x|y)=([0-9]+) by ([0-9]+))"
    screen = Screen()
    for d in data:
        reResult = re.search(reStr, d)
        if reResult.group(1) == "rect":
            screen.addRect(int(reResult.group(3)), int(reResult.group(4)))
        elif reResult.group(2) == "column":
            screen.rotateCol(int(reResult.group(5)), int(reResult.group(6)))
        elif reResult.group(2) == "row":
            screen.rotateRow(int(reResult.group(5)), int(reResult.group(6)))
    return str(screen.countPixels())


def part2(data, test=False) -> str:
    reStr = "(?:(rect) |rotate (column|row) )(?:([0-9]+)x([0-9]+)|(?:x|y)=([0-9]+) by ([0-9]+))"
    screen = Screen()
    for d in data:
        reResult = re.search(reStr, d)
        if reResult.group(1) == "rect":
            screen.addRect(int(reResult.group(3)), int(reResult.group(4)))
        elif reResult.group(2) == "column":
            screen.rotateCol(int(reResult.group(5)), int(reResult.group(6)))
        elif reResult.group(2) == "row":
            screen.rotateRow(int(reResult.group(5)), int(reResult.group(6)))
    print(screen)
    return "See Above"
