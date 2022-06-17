from y2019.intcode import IntcodeComputer
import sys


class Droid:
    def __init__(self, intCode) -> None:
        self.comp = IntcodeComputer(intCode)
        self.x = 0
        self.y = 0

        self.maxX = 1
        self.maxY = 1
        self.minX = -1
        self.minY = -1

        self.walls = []
        self.paths = [[0, 0]]
        self.oxygen = None

        self.path = []
        self.pathToO2 = []

        self.oxygenFilled = []

    def __str__(self) -> str:
        result = "------------------------"
        for y in range(self.minY, self.maxY + 1):
            outStr = "\n"
            for x in range(self.minX, self.maxX + 1):
                if x == self.x and y == self.y:
                    if [x, y] == self.oxygen:
                        outStr += " B "
                    else:
                        outStr += " X "
                elif [x, y] == [0, 0]:
                    outStr += " S "
                elif [x, y] in self.walls:
                    outStr += " # "
                elif [x, y] in self.oxygenFilled:
                    outStr += " O "
                elif [x, y] == self.oxygen:
                    outStr += " o "
                elif [x, y] in self.pathToO2:
                    outStr += " _ "
                elif [x, y] in self.paths:
                    outStr += " . "
                else:
                    outStr += " ? "
            result += outStr
        result += "\n------------------------"
        return result

    def takeStep(self, direction=None):
        stepResult = None
        if direction in [None, 1, 2, 3, 4]:
            stepResult = self.comp.run(direction)

            if stepResult != 0:
                if direction == 1:
                    self.y -= 1
                elif direction == 2:
                    self.y += 1
                elif direction == 3:
                    self.x -= 1
                elif direction == 4:
                    self.x += 1
                if not [self.x, self.y] in self.paths:
                    self.paths.append([self.x, self.y])

                if stepResult == 2:
                    self.oxygen = [self.x, self.y]

                self.maxX = max(self.maxX, self.x + 1)
                self.maxY = max(self.maxY, self.y + 1)
                self.minX = min(self.minX, self.x - 1)
                self.minY = min(self.minY, self.y - 1)
            else:
                newWall = [self.x, self.y]
                if direction == 1:
                    newWall[1] -= 1
                elif direction == 2:
                    newWall[1] += 1
                elif direction == 3:
                    newWall[0] -= 1
                elif direction == 4:
                    newWall[0] += 1
                if not newWall in self.walls:
                    self.walls.append(newWall)
        else:
            print("Invalid direction input")

        return stepResult, (self.x, self.y)

    def mapFloor(self, stepByStep=False):

        while True:
            if stepByStep:
                print(self)
                stepInput = input()
                if len(stepInput) != 0:
                    stepByStep = False

            if len(self.pathToO2) == 0 and self.oxygen != None:
                self.pathToO2 = self.path.copy()
            upDir = [self.x, self.y - 1]
            downDir = [self.x, self.y + 1]
            leftDir = [self.x - 1, self.y]
            rightDir = [self.x + 1, self.y]
            if not upDir in self.walls and not upDir in self.paths:
                self.takeStep(1)
            elif not downDir in self.walls and not downDir in self.paths:
                self.takeStep(2)
            elif not leftDir in self.walls and not leftDir in self.paths:
                self.takeStep(3)
            elif not rightDir in self.walls and not rightDir in self.paths:
                self.takeStep(4)
            else:
                lastPos = self.path.pop()
                if lastPos == [0, 0]:
                    return

                diff = [lastPos[0] - self.path[-1][0], lastPos[1] - self.path[-1][1]]

                if diff[1] > 0:
                    self.takeStep(1)
                elif diff[1] < 0:
                    self.takeStep(2)
                elif diff[0] > 0:
                    self.takeStep(3)
                else:
                    self.takeStep(4)

            if not [self.x, self.y] in self.path or [self.x, self.y] != self.path[-1]:
                self.path.append([self.x, self.y])

        return self.path

    def turnOnO2(self, stepByStep=False):
        self.oxygenFilled.append(self.oxygen.copy())

        minutesPassed = 0
        while len(self.oxygenFilled) < len(self.paths):
            if stepByStep:
                print(self)
                stepInput = input()
                if len(stepInput) != 0:
                    stepByStep = False

            minutesPassed += 1
            filledThisMin = []
            for cell in self.oxygenFilled:
                for diffX in range(-1, 2):
                    for diffY in range(-1, 2):
                        x = cell[0] + diffX
                        y = cell[1] + diffY
                        if (diffX == 0 and diffY == 0) or (diffX != 0 and diffY != 0):
                            continue
                        if [x, y] not in self.oxygenFilled and [x, y] in self.paths:
                            filledThisMin.append([x, y])

            for newFilled in filledThisMin:
                self.oxygenFilled.append(newFilled)

        return minutesPassed


def part1(data, test=False) -> str:
    droid = Droid(data[0].split(","))

    manualPlay = input("Manually control droid(y/)?")

    if manualPlay.lower() == "y" or manualPlay.lower() == "1":
        while True:
            print(droid)
            dirStr = input("Input direction (w/a/s/d):")
            if dirStr.lower() == "w":
                droid.takeStep(1)
            elif dirStr.lower() == "s":
                droid.takeStep(2)
            elif dirStr.lower() == "a":
                droid.takeStep(3)
            elif dirStr.lower() == "d":
                droid.takeStep(4)
    else:
        stepByStep = input("Show each step(y/)?")
        displayMap = input("Display end map(y/)?")
        droid.mapFloor(stepByStep)
        if displayMap.lower() == "y" or displayMap.lower() == "1":
            print(droid)
    return str(len(droid.pathToO2) - 1)


def part2(data, test=False) -> str:
    droid = Droid(data[0].split(","))
    droid.mapFloor()
    stepByStep = input("Show each step(y/)?")
    displayMap = input("Display map(y/)?")
    result = droid.turnOnO2(stepByStep)
    if displayMap.lower() == "y" or displayMap.lower() == "1":
        print(droid)
    return result
