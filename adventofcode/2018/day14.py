import math


class HotChocolate():
    def __init__(self, start, skill) -> None:
        self.recipe = start
        self.skill = skill
        self.elfOne = 0
        self.elfTwo = 1

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

    def learnRecipes(self, part2=False, debug=False):
        while len(self.recipe) < int(self.skill) + 10:
            self.doStep(debug)
        return self.result(part2)

    def doStep(self, debug=False):
        if debug:
            print(self)
        newRecpie = int(self.recipe[self.elfOne]) + \
            int(self.recipe[self.elfTwo])
        self.recipe += str(newRecpie)
        self.elfOne += int(self.recipe[self.elfOne]) + 1
        self.elfTwo += int(self.recipe[self.elfTwo]) + 1
        self.elfOne %= len(self.recipe)
        self.elfTwo %= len(self.recipe)

    def result(self, part2=False):
        result = ""
        for i in range(10):
            result += self.recipe[int(self.skill) + i]
        if part2:
            result = result[:5]
        return result

    def checkSkill(self):
        if len(self.recipe) < len(self.skill):
            return False

        if self.recipe[-len(self.skill):] == self.skill:
            return True


def part1(data):
    hotChocolate = HotChocolate("37", data)
    return hotChocolate.learnRecipes()


def part2(data):
    hotChocolate = HotChocolate("37", data)
    while not hotChocolate.checkSkill():
        hotChocolate.doStep()
    return len(hotChocolate.recipe) - len(data)


# 14131 - low
# 41313 - low
