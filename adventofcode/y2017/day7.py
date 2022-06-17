import re


class TowerProgram:
    def __init__(self, name, weight) -> None:
        self.name = name
        self.weight = weight
        self.heldPrograms = []
        self.parent = None

    def __str__(self) -> str:
        return "{} ({}): {}".format(self.name, self.weight, self.get_tower_weight())

    def print_tower(self, subTowers=True, offset="  "):
        result = str(self)
        for program in self.heldPrograms:
            if subTowers:
                result += "\n{}{}".format(
                    offset, program.print_tower(subTowers, offset + "  ")
                )
            else:
                result += "\n{}{}".format(offset, program)
        return result

    def add_sub_program(self, subProgram: "TowerProgram"):
        self.heldPrograms.append(subProgram)

    def get_root_parent(self):
        if self.parent == None:
            return self.name

        return self.parent.get_root_parent()

    def get_tower_weight(self):
        result = self.weight
        for program in self.heldPrograms:
            result += program.get_tower_weight()
        return result

    def check_sub_towers(self):
        weights = {}
        for program in self.heldPrograms:
            weight = program.get_tower_weight()
            if not weight in weights:
                weights[weight] = []
            weights[weight].append(program)

        if len(weights) > 1:
            weightDiff = 0
            for weight in weights:
                weightDiff = abs(weightDiff - weight)
            for weight in weights:
                if len(weights[weight]) == 1:
                    check, result = weights[weight][0].check_sub_towers()
                    if check:
                        return False, weights[weight][0].weight - weightDiff
                    else:
                        return False, result

        return True, 0


def parseInput(data):
    towerPrograms = {}
    subPrograms = {}

    reLeftStr = "([a-zA-Z]+) \(([0-9]+)\)"
    reRightStr = "(?:([a-zA-Z]+)(?:, |))"

    for d in data:
        dSplit = d.split(" -> ")
        reLeft = re.search(reLeftStr, dSplit[0])
        name = reLeft.group(1)
        weight = int(reLeft.group(2))
        towerPrograms[name] = TowerProgram(name, weight)
        if len(dSplit) == 2:
            reRight = re.findall(reRightStr, dSplit[1])
            if not name in subPrograms:
                subPrograms[name] = []
            for sub in reRight:
                subPrograms[name].append(sub)

    for program in subPrograms:
        for sub in subPrograms[program]:
            towerPrograms[program].add_sub_program(towerPrograms[sub])
            towerPrograms[sub].parent = towerPrograms[program]

    return towerPrograms


def part1(data, test=False) -> str:
    towerPrograms = parseInput(data)
    name = list(towerPrograms.keys())[0]
    return towerPrograms[name].get_root_parent()


def part2(data, test=False) -> str:
    towerPrograms = parseInput(data)
    name = list(towerPrograms.keys())[0]
    rootTower = towerPrograms[name].get_root_parent()

    return str(towerPrograms[rootTower].check_sub_towers()[1])
