from intcode import IntcodeComputer


class AsciiView():
    def __init__(self, intCode) -> None:
        self.comp = IntcodeComputer(intCode)
        self.asciiView = self.comp.run(None, False)
        self.asciiView.pop()

        self.view = []
        newRow = []
        for i in self.asciiView:
            if i == 10:
                self.view.append(newRow.copy())
                newRow = []
            else:
                newRow.append(i)

    def __str__(self):
        result = ""
        for i in self.asciiView:
            result += chr(i)
        return result

    def countIntersections(self):
        result = 0
        for x in range(len(self.view)):
            for y in range(len(self.view[x])):
                if self.view[x][y] == ord("#"):
                    intersection = True
                    for difX in range(-1, 2):
                        for difY in range(-1, 2):
                            if difX == 0 and difY == 0:
                                continue
                            if difX != 0 and difY != 0:
                                continue
                            checkX = x - difX
                            checkY = y - difY
                            if checkX < 0 or checkX >= len(self.view):
                                continue
                            if checkY < 0 or checkY >= len(self.view[x]):
                                continue
                            if self.view[checkX][checkY] != ord("#"):
                                intersection = False
                                break
                        if not intersection:
                            break
                    if intersection:
                        result += x * y
        return result


def appendInput(buildStr, newInput):
    for i in newInput:
        buildStr.append(ord(i))
    buildStr.append(ord('\n'))
    return buildStr


def part1(data):
    asciiView = AsciiView(data.split(","))
    return asciiView.countIntersections()


def part2(data):
    data = data.split(",")
    data[0] = 2

    inputData = []
    inputData = appendInput(inputData, "A,B,A,C,A,A,C,B,C,B")
    inputData = appendInput(inputData, "L,12,L,8,R,12")
    inputData = appendInput(inputData, "L,10,L,8,L,12,R,12")
    inputData = appendInput(inputData, "R,12,L,8,L,10")
    inputData = appendInput(inputData, "n")

    comp = IntcodeComputer(data)
    result = 0
    for i in inputData:
        result = comp.run(i, False)

    return result[-1]
