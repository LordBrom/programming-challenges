import sys

SHORTEST = sys.maxsize
COUNT = 0


def fillContainers(containers, setGlobal=False, eggnog=150, index=0, used=[], stored=0):
    global SHORTEST
    global COUNT
    if stored == eggnog:
        if setGlobal and len(used) < SHORTEST:
            SHORTEST = len(used)
            COUNT = 1
        elif setGlobal and len(used) == SHORTEST:
            COUNT += 1
        return 1
    elif stored > eggnog:
        return 0
    elif index >= len(containers):
        return 0

    result = 0

    usedCopy = used.copy()
    usedCopy.append(index)
    result += fillContainers(containers, setGlobal, eggnog, index + 1,
                             usedCopy, stored + containers[index])
    result += fillContainers(containers, setGlobal, eggnog,
                             index + 1, used.copy(), stored)

    return result


def part1(data):
    containers = [int(x) for x in data]
    return fillContainers(containers)


def part2(data):
    containers = [int(x) for x in data]
    fillContainers(containers, True)
    return COUNT
