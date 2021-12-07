

from sys import maxsize


def part1(input):
    input = [int(x) for x in input[0].split(",")]
    input.sort()

    minPos = input[0]
    maxPos = input[-1]

    diff = maxPos - minPos
    minResult = maxsize

    for r in range(diff):
        increase = diff - r

        reduceTarget = maxPos - r
        increaseTarget = minPos + increase

        result = 0
        for h in input:
            if h > reduceTarget:
                result += h - reduceTarget
            if h < increaseTarget:
                result += increaseTarget - h
        minResult = min(minResult, result)

    return minResult


def part2(input):
    input = [int(x) for x in input[0].split(",")]
    input.sort()

    minPos = input[0]
    maxPos = input[-1]

    diff = maxPos - minPos
    minResult = maxsize

    for r in range(diff):
        increase = diff - r

        reduceTarget = maxPos - r
        increaseTarget = minPos + increase

        result = 0
        for h in input:
            if h > reduceTarget:
                result += sum(range((h - reduceTarget) + 1))
            if h < increaseTarget:
                result += sum(range((increaseTarget - h) + 1))
        minResult = min(minResult, result)

    return minResult
