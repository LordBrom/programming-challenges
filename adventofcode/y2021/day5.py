import re

RESTR = "([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)"


def countOverlap(input, countDiagonals=False):

    results = {}

    for i in input:
        reResults = re.search(RESTR, i)

        x = [int(reResults.group(1)), int(reResults.group(2))]
        y = [int(reResults.group(3)), int(reResults.group(4))]

        if x[0] == y[0]:
            for n in range(min(x[1], y[1]), max(x[1], y[1]) + 1):
                point = str(x[0]) + "_" + str(n)
                if not point in results:
                    results[point] = 0
                results[point] += 1

        elif x[1] == y[1]:
            for n in range(min(x[0], y[0]), max(x[0], y[0]) + 1):
                point = str(n) + "_" + str(x[1])
                if not point in results:
                    results[point] = 0
                results[point] += 1

        elif countDiagonals:
            firstSwap = False
            if x[0] < y[0]:
                firstSwap = True

            secondSwap = False
            if x[1] < y[1]:
                secondSwap = True

            first = list(range(min(x[0], y[0]), max(x[0], y[0]) + 1))
            if firstSwap:
                first = first[::-1]

            second = list(range(min(x[1], y[1]), max(x[1], y[1]) + 1))
            if secondSwap:
                second = second[::-1]

            for n in range(len(first)):
                point = str(first[n]) + "_" + str(second[n])
                if not point in results:
                    results[point] = 0
                results[point] += 1

    resultCount = 0

    for r in results:
        if results[r] > 1:
            resultCount += 1

    return resultCount


def part1(data, test=False) -> str:
    return countOverlap(data)


def part2(data):
    return countOverlap(data, True)
