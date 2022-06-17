import re


class ChipType:
    def __init__(self, name, letter) -> None:
        self.name = name
        self.letter = letter
        self.chipFloor = None
        self.genFloor = None

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, ChipType) and self.name == __o.name

    def getChipShortName(self):
        return self.letter + "M"

    def getGenShortName(self):
        return self.letter + "G"

    def isCharged(self):
        return self.chipFloor == self.genFloor


class Building:
    def __init__(self, floorData) -> None:
        reStr = "a ([a-z]+)(?:-compatible|) (microchip|generator)"
        self.elevator = 0
        self.floors = 4
        self.floorObjects = []
        self.chipTypes = {}
        letterIndex = 0
        for f in range(4):
            reResult = re.findall(reStr, floorData[f])
            for res in reResult:
                if not res[0] in self.chipTypes:
                    self.chipTypes[res[0]] = ChipType(
                        res[0], chr(letterIndex + 97).upper()
                    )
                    letterIndex += 1

                if res[1][0] == "m":
                    self.chipTypes[res[0]].chipFloor = f
                else:
                    self.chipTypes[res[0]].genFloor = f

    def __str__(self) -> str:
        result = ""
        for f in reversed(range(self.floors)):
            result += "\nF{} ".format(f + 1)
            if self.elevator == f:
                result += "E  "
            else:
                result += ".  "
            for ct in self.chipTypes:
                chipType = self.chipTypes[ct]

                if chipType.genFloor == f:
                    result += " {} ".format(chipType.getGenShortName())
                else:
                    result += " .  "

                if chipType.chipFloor == f:
                    result += " {} ".format(chipType.getChipShortName())
                else:
                    result += " .  "
            pass
        return result

    def moveElevator(self, moveUp=True):
        startFloor = self.elevator
        if moveUp and startFloor == 3:
            return False
        if not moveUp and startFloor == 0:
            return False

        # if objectOne.floor != startFloor or objectTwo.floor != startFloor:
        #    return False


def part1(data, test=False) -> str:
    building = Building(data)
    print(building)

    return "not implemented"


def part2(data, test=False) -> str:
    return "not implemented"
