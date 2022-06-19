from gettext import find
from textwrap import fill
from aoc import manhattan_distance


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


def part1(data, test=False) -> str:
    data = data[0]
    return str(manhattan_distance(tuple([0, 0]), findNum(int(data))))


def part2(data, test=False) -> str:
    data = data[0]
    return str(findNum(int(data), True))
