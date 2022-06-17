from functools import lru_cache


def checkReact(a, b):
    if a.upper() != b.upper():
        return False
    if a.upper() == a and b.lower() == b:
        return True
    if a.lower() == a and b.upper() == b:
        return True
    return False


@lru_cache(maxsize=None)
def generation(unitStr, debug=False):
    result = ""
    if debug:
        print(unitStr)
    for i in range(len(unitStr)):
        if i < len(unitStr) - 1 and checkReact(unitStr[i], unitStr[i+1]):
            if debug:
                print("removing " + unitStr[i] + unitStr[i+1])
            return unitStr[:i] + unitStr[i+2:]
    return unitStr


def runLife(input):
    lastLen = -1
    while len(input) != lastLen:
        lastLen = len(input)
        input = generation(input)
    return len(input)


def part1(input):
    return runLife(input)


def part2(input):
    checkedList = []

    bestRemoved = -1
    best = 0

    for i in range(len(input)):
        if not input[i] in checkedList:
            checkedList.append(input[i])

            newInput = input[:]
            newInput = newInput.replace(input[i].upper(), "")
            newInput = newInput.replace(input[i].lower(), "")

            inputCheck = runLife(newInput)
            if bestRemoved == -1 or bestRemoved > inputCheck:
                bestRemoved = inputCheck
                best = input[i]

    return bestRemoved
