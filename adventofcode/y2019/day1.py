from math import floor


def calc_fuel(mass, calcExtra=False):
    step1 = floor(int(mass) / 3)
    step2 = max(step1 - 2, 0)
    if calcExtra and step2 > 0:
        return step2 + calc_fuel(step2, calcExtra)
    return step2


def part1(data):
    total = 0
    for num in data:
        total += calc_fuel(num)
    return total


def part2(data):
    total = 0
    for num in data:
        total += calc_fuel(num, True)
    return total
