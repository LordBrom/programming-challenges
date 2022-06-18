import re

RESTR = "([a-z]+) ([0-9]+)"


def part1(data, test=False) -> str:
    position = 0
    depth = 0

    for i in data:
        reResults = re.search(RESTR, i)

        if reResults.group(1) == "forward":
            position += int(reResults.group(2))
        elif reResults.group(1) == "down":
            depth += int(reResults.group(2))
        elif reResults.group(1) == "up":
            depth -= int(reResults.group(2))

    return str(position * depth)


def part2(data, test=False) -> str:
    aim = 0
    position = 0
    depth = 0

    for i in data:
        reResults = re.search(RESTR, i)

        if reResults.group(1) == "forward":
            position += int(reResults.group(2))
            depth += aim * int(reResults.group(2))
        elif reResults.group(1) == "down":
            aim += int(reResults.group(2))
        elif reResults.group(1) == "up":
            aim -= int(reResults.group(2))

    return str(position * depth)
