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
        if i < len(unitStr) - 1 and checkReact(unitStr[i], unitStr[i + 1]):
            if debug:
                print("removing " + unitStr[i] + unitStr[i + 1])
            return unitStr[:i] + unitStr[i + 2 :]
    return unitStr


def runLife(input):
    lastLen = -1
    while len(input) != lastLen:
        lastLen = len(input)
        input = generation(input)
    return len(input)


def part1(data, test=False) -> str:
    data = data[0]
    return str(runLife(data))


def part2(data, test=False) -> str:
    data = data[0]
    checkedList = []

    bestRemoved = -1
    best = 0

    for i in range(len(data)):
        if not data[i] in checkedList:
            checkedList.append(data[i])

            newInput = data[:]
            newInput = newInput.replace(data[i].upper(), "")
            newInput = newInput.replace(data[i].lower(), "")

            inputCheck = runLife(newInput)
            if bestRemoved == -1 or bestRemoved > inputCheck:
                bestRemoved = inputCheck
                best = data[i]

    return str(bestRemoved)
