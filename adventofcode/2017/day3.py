
from gettext import find
from textwrap import fill


def findNum(num, part2=False):
    x = 0
    y = 0

    n = 1
    steps = 1
    secondStep = False
    toTake = steps
    dir = 0

    results = {"0_0": 1}

    while n < num or part2:
        n += 1
        if dir == 0:
            x += 1
        elif dir == 1:
            y += 1
        elif dir == 2:
            x -= 1
        elif dir == 3:
            y -= 1
        if part2:
            results["{}_{}".format(x, y)] = sumAdjacent(x, y, results)
            if results["{}_{}".format(x, y)] > num:
                return results["{}_{}".format(x, y)]

        toTake -= 1
        if toTake == 0:
            dir += 1
            dir %= 4

            if secondStep:
                steps += 1
                secondStep = False
            else:
                secondStep = True

            toTake = steps
    return [x, y]


def sumAdjacent(x, y, filledValues):
    result = 0
    for diffX in range(-1, 2):
        for diffY in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if "{}_{}".format(diffX + x, diffY + y) in filledValues:
                result += filledValues["{}_{}".format(diffX + x, diffY + y)]

    return result


def manhattanDistance(point1, point2):
    diffX = abs(point1[0] - point2[0])
    diffY = abs(point1[1] - point2[1])
    return diffX + diffY


def part1(data):
    return manhattanDistance([0, 0], findNum(int(data)))


def part2(data):
    return findNum(int(data), True)
