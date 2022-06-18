from functools import lru_cache

RULES = {}


def parseInput(data):
    start = data.pop(0)
    data.pop(0)
    rules = {}

    for i in data:
        ruleSplit = i.split(" -> ")
        rules[ruleSplit[0]] = ruleSplit[1]

    return [start, rules]


def addToResult(result, newValue, setOne=False):
    for l in newValue:
        if not l in result:
            result[l] = 0
        if setOne:
            result[l] = 1
        else:
            result[l] += newValue[l]
    return result


@lru_cache(maxsize=None)
def doStep(pair, steps):
    if steps <= 0:
        return ""

    if not pair in RULES:
        return ""

    result = {RULES[pair]: 1}
    firstHalf = doStep(pair[0] + RULES[pair], steps - 1)
    lastHalf = doStep(RULES[pair] + pair[1], steps - 1)
    result = addToResult(result, firstHalf)
    result = addToResult(result, lastHalf)

    return result.copy()


def part1(data, test=False) -> str:
    dataParsed = parseInput(data)
    polymer = dataParsed[0]
    global RULES
    RULES = dataParsed[1]

    result = {}

    result = addToResult(result, polymer, True)

    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        step = doStep(pair, 10)
        result = addToResult(result, step)

    results = list(result.values())
    results.sort()

    return str(results[-1] - results[0])


def part2(data, test=False) -> str:
    dataParsed = parseInput(data)
    polymer = dataParsed[0]
    global RULES
    RULES = dataParsed[1]

    result = {}

    result = addToResult(result, polymer, True)

    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        step = doStep(pair, 40)
        result = addToResult(result, step)

    results = list(result.values())
    results.sort()

    return str(results[-1] - results[0])
