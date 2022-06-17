import re

RESTR = "([a-z]+) ([0-9]+)"


def part1(input):
    position = 0
    depth = 0

    for i in input:
        reResults = re.search(RESTR, i)

        if reResults.group(1) == "forward":
            position += int(reResults.group(2))
        elif reResults.group(1) == "down":
            depth += int(reResults.group(2))
        elif reResults.group(1) == "up":
            depth -= int(reResults.group(2))

    return position * depth


def part2(input):
    aim = 0
    position = 0
    depth = 0

    for i in input:
        reResults = re.search(RESTR, i)

        if reResults.group(1) == "forward":
            position += int(reResults.group(2))
            depth += aim * int(reResults.group(2))
        elif reResults.group(1) == "down":
            aim += int(reResults.group(2))
        elif reResults.group(1) == "up":
            aim -= int(reResults.group(2))

    return position * depth
