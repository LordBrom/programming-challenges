from functools import reduce


def getFactors(n):
    return list(
        set(
            reduce(
                list.__add__,
                ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0),
            )
        )
    )


def countPresents(houseNum, presents=10, maxHouses=False):
    result = 0
    factors = getFactors(houseNum)
    factors.sort(reverse=True)
    for n in factors:
        if maxHouses and houseNum / n > 50:
            break
        result += n * presents
    return result


def part1(data, test=False) -> str:
    data = data[0]
    house = 1
    house = 786240

    while True:
        check = countPresents(house)
        if check >= int(data):
            break
        house += 1
    return str(house)


def part2(data, test=False) -> str:
    data = data[0]
    house = 1

    while True:
        check = countPresents(house, 11, True)
        if check >= int(data):
            break
        house += 1
    return str(house)
