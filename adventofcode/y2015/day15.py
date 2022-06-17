import re

RE_STR = "(.+): capacity ([-0-9]+), durability ([-0-9]+), flavor ([-0-9]+), texture ([-0-9]+), calories ([-0-9]+)"


class Ingredients:
    def __init__(self, inStr) -> None:
        reResult = re.search(RE_STR, inStr)
        self.name = reResult.group(1)

        self.capacity = int(reResult.group(2))
        self.durability = int(reResult.group(3))
        self.flavor = int(reResult.group(4))
        self.texture = int(reResult.group(5))
        self.calories = int(reResult.group(6))

    def value(self, amount):
        result = []
        result.append(amount * self.capacity)
        result.append(amount * self.durability)
        result.append(amount * self.flavor)
        result.append(amount * self.texture)
        result.append(amount * self.calories)
        return result


def checkIngVals(ingVals, checkCalaries=False):
    result = 1

    for i in range(4):
        next = 0
        for ingVal in ingVals:
            next += ingVal[i]
        result *= max(next, 0)

    if checkCalaries:
        cals = 0
        for ingVal in ingVals:
            cals += ingVal[4]
        if cals != 500:
            return 0
    return result


def getBest(data, ignoreCals=True) -> int:
    ingredients = []
    for d in data:
        ingredients.append(Ingredients(d))

    ingTotal = 100

    best = 0

    for i1 in range(1, ingTotal - (3)):
        if len(ingredients) == 2:
            i2 = ingTotal - (i1)

            ingVals = []
            ingVals.append(ingredients[0].value(i1))
            ingVals.append(ingredients[1].value(i2))

            check = checkIngVals(ingVals, not ignoreCals)
            if check > best:
                best = check
        else:
            for i2 in range(1, ingTotal - ((i1))):
                for i3 in range(1, ingTotal - ((i1 + i2))):
                    i4 = ingTotal - (i1 + i2 + i3)

                    ingVals = []
                    ingVals.append(ingredients[0].value(i1))
                    ingVals.append(ingredients[1].value(i2))
                    ingVals.append(ingredients[2].value(i3))
                    ingVals.append(ingredients[3].value(i4))

                    check = checkIngVals(ingVals, not ignoreCals)

                    if check > best:
                        best = check

    return best


def part1(data, test=False) -> str:
    return str(getBest(data))


def part2(data, test=False) -> str:
    return str(getBest(data, False))
