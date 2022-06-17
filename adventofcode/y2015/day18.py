class Light:
    def __init__(self, x, y, state, keepOn=False) -> None:
        self.x = x
        self.y = y
        self.state = state == "#"
        self.adjacent = []
        self.step = 0
        self.lastState = None
        self.keepOn = keepOn
        if keepOn:
            self.state = True
            self.lastState = True

    def setAdjacent(self, board):
        for diffX in range(-1, 2):
            for diffY in range(-1, 2):
                if diffX == 0 and diffY == 0:
                    continue

                x = self.x + diffX
                y = self.y + diffY

                if x < 0 or y < 0 or x >= len(board) or y >= len(board[x]):
                    continue

                self.adjacent.append(board[x][y])

    def nextStep(self):
        if self.keepOn:
            self.step += 1
        else:
            adjacentOn = 0
            for light in self.adjacent:
                if light.step == self.step:
                    if light.state:
                        adjacentOn += 1
                else:
                    if light.lastState:
                        adjacentOn += 1
            self.step += 1
            self.lastState = self.state
            if self.state and adjacentOn != 3 and adjacentOn != 2:
                self.state = False
            elif not self.state and adjacentOn == 3:
                self.state = True


class Board:
    def __init__(self, inData, cornersOn=False) -> None:
        self.lights = []

        for x in range(len(inData)):
            row = []
            for y in range(len(inData[x])):
                keepOn = (
                    cornersOn
                    and x in [0, len(inData) - 1]
                    and y in [0, len(inData[x]) - 1]
                )
                row.append(Light(x, y, inData[x][y], keepOn))
            self.lights.append(row)

        for x in range(len(self.lights)):
            row = []
            for y in range(len(self.lights[x])):
                self.lights[x][y].setAdjacent(self.lights)

    def __str__(self) -> str:
        result = ""
        for x in range(len(self.lights)):
            rowStr = ""
            for y in range(len(self.lights[x])):
                if self.lights[x][y].state:
                    rowStr += "#"
                else:
                    rowStr += "."
            result += "\n" + rowStr

        return result

    def takeSteps(self, steps=100, showSteps=False):
        for i in range(steps):
            for row in self.lights:
                for light in row:
                    light.nextStep()
            if showSteps:
                print(self)
                input()

    def getLightOnCount(self):
        result = 0
        for row in self.lights:
            for light in row:
                if light.state:
                    result += 1
        return result


def part1(data, test=False) -> str:
    board = Board(data)
    board.takeSteps()
    return board.getLightOnCount()


def part2(data, test=False) -> str:
    board = Board(data, True)
    board.takeSteps()
    return board.getLightOnCount()
