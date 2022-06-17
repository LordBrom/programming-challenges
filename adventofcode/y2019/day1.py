from math import floor


def calc_fuel(mass, calcExtra=False):
    step1 = floor(int(mass) / 3)
    step2 = max(step1 - 2, 0)
    if calcExtra and step2 > 0:
        return step2 + calc_fuel(step2, calcExtra)
    return step2


def part1(data, test=False) -> str:
    total = 0
    for num in data:
        total += calc_fuel(num)
    return str(total)


def part2(data, test=False) -> str:
    total = 0
    for num in data:
        total += calc_fuel(num, True)
    return str(total)
