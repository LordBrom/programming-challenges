from sys import maxsize


def part1(data, test=False) -> str:
    data = [int(x) for x in data[0].split(",")]
    data.sort()

    minPos = data[0]
    maxPos = data[-1]

    diff = maxPos - minPos
    minResult = maxsize

    for r in range(diff):
        increase = diff - r

        reduceTarget = maxPos - r
        increaseTarget = minPos + increase

        result = 0
        for h in data:
            if h > reduceTarget:
                result += h - reduceTarget
            if h < increaseTarget:
                result += increaseTarget - h
        minResult = min(minResult, result)

    return minResult


def part2(data):
    data = [int(x) for x in data[0].split(",")]
    data.sort()

    minPos = data[0]
    maxPos = data[-1]

    diff = maxPos - minPos
    minResult = maxsize

    for r in range(diff):
        increase = diff - r

        reduceTarget = maxPos - r
        increaseTarget = minPos + increase

        result = 0
        for i in data:
            if i > reduceTarget:
                n = i - reduceTarget
                result += int((n * (n + 1)) / 2)
            if i < increaseTarget:
                n = increaseTarget - i
                result += int((n * (n + 1)) / 2)
        minResult = min(minResult, result)

    return minResult
