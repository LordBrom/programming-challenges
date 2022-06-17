import math


class HotChocolate:
    def __init__(self, start, skill) -> None:
        self.recipe = start
        self.skill = skill
        self.elfOne = 0
        self.elfTwo = 1
        self.skillPart2 = [int(x) for x in skill]

    def __str__(self) -> str:
        result = ""
        for i in range(len(self.recipe)):
            if i == self.elfOne:
                result += "({})".format(self.recipe[i])
            elif i == self.elfTwo:
                result += "[{}]".format(self.recipe[i])
            else:
                result += " {} ".format(self.recipe[i])
        return result

    def doRecpie(self, debug=False):
        if debug:
            print(self)
        newRecpie = self.recipe[self.elfOne] + self.recipe[self.elfTwo]
        if newRecpie > 9:
            self.recipe.append(math.floor(newRecpie / 10))
            newRecpie %= 10
        self.recipe.append(newRecpie)
        self.elfOne += self.recipe[self.elfOne] + 1
        self.elfTwo += self.recipe[self.elfTwo] + 1
        self.elfOne %= len(self.recipe)
        self.elfTwo %= len(self.recipe)

    def result(self):
        result = ""
        for i in range(10):
            result += str(self.recipe[int(self.skill) + i])
        return result

    def checkSkill(self):
        if len(self.recipe) < len(self.skill):
            return False

        if self.recipe[-len(self.skill) :] == self.skillPart2:
            return len(self.recipe) - len(self.skill)

        if (
            self.recipe[-2] == 1
            and self.recipe[-(len(self.skill) + 1) : -1] == self.skillPart2
        ):
            return (len(self.recipe) - len(self.skill)) - 1

        return False


def part1(data, test=False) -> str:
    hotChocolate = HotChocolate([3, 7], data)
    while len(hotChocolate.recipe) < int(data) + 10:
        hotChocolate.doRecpie()
    return hotChocolate.result()


def part2(data, test=False) -> str:
    hotChocolate = HotChocolate([3, 7], data)
    result = False
    while result == False:
        hotChocolate.doRecpie()
        result = hotChocolate.checkSkill()
    return str(result)
