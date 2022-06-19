from typing import Dict


def part1(data, test=False) -> str:

    result = 0

    for i in data:
        result += int(i)

    return str(result)


def part2(data, test=False) -> str:

    result = 0
    found: Dict[int, bool] = {}
    i = 0

    while True:
        result += int(data[i % len(data)])
        i += 1
        if result in found:
            return str(result)
        else:
            found[result] = True
