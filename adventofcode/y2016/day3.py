from posixpath import split


def isValidTriangle(inData):
    sideLengths = [int(x) for x in inData]
    sideLengths.sort()
    if sideLengths[2] >= sum(sideLengths) / 2:
        return False
    return True


def multiStrip(string):
    string = string.strip()
    for i in range(3):
        string = string.replace("  ", " ")
    return string


def part1(data, test=False) -> str:
    result = 0
    for d in data:
        if isValidTriangle(multiStrip(d).split(" ")):
            result += 1
    return result


def part2(data, test=False) -> str:
    result = 0
    for i in range(0, len(data), 3):
        firstRow = multiStrip(data[i]).split(" ")
        secondRow = multiStrip(data[i + 1]).split(" ")
        lastRow = multiStrip(data[i + 2]).split(" ")

        if isValidTriangle([firstRow[0], secondRow[0], lastRow[0]]):
            result += 1
        if isValidTriangle([firstRow[1], secondRow[1], lastRow[1]]):
            result += 1
        if isValidTriangle([firstRow[2], secondRow[2], lastRow[2]]):
            result += 1
    return result
