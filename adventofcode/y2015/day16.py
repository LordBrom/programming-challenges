import re
from turtle import pos, position

SUE_DATA = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


class AuntSue:
    def __init__(self, dataString) -> None:
        reStr1 = "Sue ([0-9]+):(.+)"
        reStr2 = "(?: (.+?): ([0-9]+)(?:,|))+?"
        reResult = re.search(reStr1, dataString)
        self.auntID = int(reResult.group(1))

        reResultRight = re.findall(reStr2, reResult.group(2))
        self.possessions = {}
        for match in reResultRight:
            self.possessions[match[0]] = int(match[1])

    def __str__(self) -> str:
        result = "Sue {}:".format(self.auntID)
        first = True
        for possession in self.possessions:
            if not first:
                result += ","
            first = False

            result += " {}: {}".format(possession, self.possessions[possession])
        return result

    def checkPossessions(self, possessions):
        for possession in possessions:
            if possession in self.possessions:
                if self.possessions[possession] != possessions[possession]:
                    return False
        return True

    def checkApproxPossessions(self, possessions):
        for possession in possessions:
            if possession in self.possessions:
                if possession in ["cats", "trees"]:
                    if self.possessions[possession] <= possessions[possession]:
                        return False
                elif possession in ["pomeranians", "goldfish"]:
                    if self.possessions[possession] >= possessions[possession]:
                        return False
                else:
                    if self.possessions[possession] != possessions[possession]:
                        return False
        return True


def part1(data, test=False) -> str:
    auntSues = []
    for d in data:
        auntSues.append(AuntSue(d))
    results = []
    for auntSue in auntSues:
        if auntSue.checkPossessions(SUE_DATA):
            results.append(auntSue)
    if len(results) == 1:
        return results[0].auntID
    else:
        return "didn't find just 1 aunt"


def part2(data, test=False) -> str:
    auntSues = []
    for d in data:
        auntSues.append(AuntSue(d))
    results = []
    for auntSue in auntSues:
        if auntSue.checkApproxPossessions(SUE_DATA):
            results.append(auntSue)
    if len(results) == 1:
        return results[0].auntID
    else:
        return "didn't find just 1 aunt"
