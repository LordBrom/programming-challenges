import math


class Image:
    def __init__(self, enhancementAlg, image):
        self.enhancementAlg = enhancementAlg
        self.pixels = {}
        self.image = []

        self.trim = enhancementAlg[0] == "#"

        fullImageSize = len(image) + 120

        for i in range(fullImageSize):
            self.image.append([False for x in range(fullImageSize)])

        imageOffset = math.floor(len(image) / 2)
        fullImageOffset = math.floor(fullImageSize / 2)
        for x in range(len(image)):
            for y in range(len(image[x])):
                self.image[(x + fullImageOffset) - imageOffset][
                    (y + fullImageOffset) - imageOffset
                ] = (image[x][y] == "#")

    def __str__(self) -> str:
        result = "-------------------------"
        for x in range(len(self.image)):
            outStr = "\n"
            for y in range(len(self.image[x])):
                if self.image[x][y]:
                    outStr += "#"
                else:
                    outStr += "."
            result += outStr
        result += "\n-------------------------"
        return result

    def enhance(self, times, debug=False):
        for i in range(times):
            if debug:
                print(self)
                input()
            self.doEnhance()
            if self.trim and i % 2 == 1:
                self.trimOutter()

    def doEnhance(self):
        newImage = []
        for x in range(len(self.image)):
            newRow = []
            for y in range(len(self.image[x])):
                newRow.append(self.getNewVal(x, y))
            newImage.append(newRow)
        self.image = newImage

    def getNewVal(self, _x, _y):
        binStr = ""
        for offX in range(-1, 2):
            for offY in range(-1, 2):
                x = _x + offX
                y = _y + offY
                if x < 0 or y < 0 or x >= len(self.image) or y >= len(self.image[x]):
                    binStr += "0"
                elif self.image[x][y]:
                    binStr += "1"
                else:
                    binStr += "0"
        return self.enhancementAlg[int(binStr, 2)] == "#"

    def countPixels(self):
        result = 0
        for x in range(len(self.image)):
            for y in range(len(self.image[x])):
                if self.image[x][y]:
                    result += 1
        return result

    def trimOutter(self):
        for y in range(len(self.image[0])):
            self.image[0][y] = False
        for x in range(len(self.image)):
            self.image[x][0] = False


def part1(data, test=False) -> str:
    enhancementAlg = data.pop(0)
    data.pop(0)
    image = Image(enhancementAlg, data)
    image.enhance(2)
    return str(image.countPixels())


def part2(data, test=False) -> str:
    enhancementAlg = data.pop(0)
    data.pop(0)
    image = Image(enhancementAlg, data)
    image.enhance(50)
    return str(image.countPixels())
