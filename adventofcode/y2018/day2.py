import math


def part1(data, test=False) -> str:
    pairs = 0
    trips = 0
    for id in data:
        foundLetter = {}
        for l in id:
            if not l in foundLetter:
                foundLetter[l] = 0
            foundLetter[l] += 1

        foundPair = False
        foundTrip = False

        for l in foundLetter:
            if not foundPair and foundLetter[l] == 2:
                foundPair = True
                pairs += 1
            elif not foundTrip and foundLetter[l] == 3:
                foundTrip = True
                trips += 1

    return str(pairs * trips)


def part2(data, test=False) -> str:
    bestDiff = 0
    bestOne = 0
    bestTwo = 0
    for index in range(len(data)):
        id = data[index]

        for indexCheck in range(index + 1, len(data)):
            idCheck = data[indexCheck]
            currentBest = 0
            for i in range(len(id)):
                if id[i] == idCheck[i]:
                    currentBest += 1

            if currentBest > bestDiff:
                bestDiff = currentBest
                bestOne = index
                bestTwo = indexCheck

    result = ""
    for i in range(len(id)):
        if data[bestOne][i] == data[bestTwo][i]:
            result += data[bestOne][i]

    return result
