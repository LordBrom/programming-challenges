import re


def parseInput(data):
    steps = []
    reStr = "(.+) (inc|dec) ([0-9-]+) if (.+) (.+) ([0-9-]+)"

    for d in data:
        reResult = re.search(reStr, d)
        target = reResult.group(1)
        increase = reResult.group(2)
        amount = int(reResult.group(3))
        condition = [reResult.group(4), reResult.group(
            5), int(reResult.group(6))]
        steps.append([target, increase, amount, condition])

    return steps


def check_condition(registers, condition):
    if not condition[0] in registers:
        registers[condition[0]] = 0

    if condition[1] == ">":
        return registers[condition[0]] > condition[2]
    elif condition[1] == "<":
        return registers[condition[0]] < condition[2]
    elif condition[1] == ">=":
        return registers[condition[0]] >= condition[2]
    elif condition[1] == "<=":
        return registers[condition[0]] <= condition[2]
    elif condition[1] == "==":
        return registers[condition[0]] == condition[2]
    elif condition[1] == "!=":
        return registers[condition[0]] != condition[2]


def run_instructions(instructions):
    registers = {}
    maxVal = 0

    for instruction in instructions:
        if check_condition(registers, instruction[3]):
            if not instruction[0] in registers:
                registers[instruction[0]] = 0
            if instruction[1] == "inc":
                registers[instruction[0]] += instruction[2]
            else:
                registers[instruction[0]] -= instruction[2]
        for register in registers:
            maxVal = max(maxVal, registers[register])

    return registers, maxVal


def part1(data):
    steps = parseInput(data)
    registers = run_instructions(steps)[0]
    result = 0
    for register in registers:
        result = max(result, registers[register])
    return result


def part2(data):
    steps = parseInput(data)
    return run_instructions(steps)[1]
