import re


def part1(data, test=False) -> str:
    # group 1: claim ID
    # group 2: left offset
    # group 3: top offset
    # group 4: width
    # group 5: height
    reStr = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
    squareSize = 1000
    fabric = []
    for i in range(squareSize):
        fabric.append([0 for i in range(squareSize)])

    for claim in data:
        reResult = re.search(reStr, claim)
        for x in range(
            int(reResult.group(2)), int(reResult.group(2)) + int(reResult.group(4))
        ):
            for y in range(
                int(reResult.group(3)), int(reResult.group(3)) + int(reResult.group(5))
            ):
                fabric[x][y] += 1

    result = 0
    for x in range(len(fabric)):
        for y in range(len(fabric[x])):
            if fabric[x][y] > 1:
                result += 1

    return str(result)


def part2(data, test=False) -> str:
    # group 1: claim ID
    # group 2: left offset
    # group 3: top offset
    # group 4: width
    # group 5: height
    reStr = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
    squareSize = 1000
    fabric = []
    for i in range(squareSize):
        fabric.append([0 for i in range(squareSize)])

    claimCheck = [True for i in range(len(data) + 1)]

    for claim in data:
        reResult = re.search(reStr, claim)
        for x in range(
            int(reResult.group(2)), int(reResult.group(2)) + int(reResult.group(4))
        ):
            for y in range(
                int(reResult.group(3)), int(reResult.group(3)) + int(reResult.group(5))
            ):
                if fabric[x][y] == 0:
                    fabric[x][y] = int(reResult.group(1))
                else:
                    claimCheck[fabric[x][y]] = False
                    claimCheck[int(reResult.group(1))] = False

    for i in range(1, len(claimCheck)):
        if claimCheck[i]:
            return str(i)

    return ""


def printFabric(fabric):
    print("")
    for x in range(len(fabric)):
        outStr = ""
        for y in range(len(fabric[x])):
            outStr += str(fabric[x][y])
        print(outStr)
    print("")
