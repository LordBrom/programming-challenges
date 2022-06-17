
def getTrapRow(prevTrapRow):
    result = []

    for tile in range(len(prevTrapRow)):
        tileC = prevTrapRow[tile]
        if tile > 0:
            tileL = prevTrapRow[tile - 1]
        else:
            tileL = False
        if tile < len(prevTrapRow) - 1:
            tileR = prevTrapRow[tile + 1]
        else:
            tileR = False

        if (tileL and tileC and not tileR) \
                or (not tileL and tileC and tileR) \
                or (tileL and not tileC and not tileR) \
                or (not tileL and not tileC and tileR):
            result.append(True)
        else:
            result.append(False)

    return result


def parseInput(data):
    floor = []
    for tile in data:
        floor.append(tile == "^")
    return floor


def countSafeTiles(floor):
    result = 0
    for row in floor:
        for tile in row:
            if not tile:
                result += 1
    return result


def part1(data):
    floor = [parseInput(data)]
    while len(floor) < 40:
        floor.append(getTrapRow(floor[-1]))
    return countSafeTiles(floor)


def part2(data):
    tileRow = parseInput(data)
    result = tileRow.count(False)
    for i in range(1, 400000):
        tileRow = getTrapRow(tileRow)
        result += tileRow.count(False)
    return result
