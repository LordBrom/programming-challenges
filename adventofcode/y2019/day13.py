from y2019.intcode import IntcodeComputer
import numpy as np


class GameScreen:
    def __init__(self, intcode, setFree=False):
        self.score = 0
        if setFree:
            intcode[0] = 2
        self.comp = IntcodeComputer(intcode)
        compResult = np.array(self.comp.run(0, False)).reshape(-1, 3)

        maxX = 0
        maxY = 0
        for t in compResult:
            maxX = max(maxX, t[0])
            maxY = max(maxY, t[1])

        screenX = maxX + 1
        screenY = maxY + 1

        self.screen = np.ndarray((screenY, screenX))
        self.updateScreen(compResult)

    def updateScreen(self, tiles):
        for t in tiles:
            if t[0] == -1:
                self.score = t[2]
            self.screen[t[1]][t[0]] = t[2]

    def getNextMove(self):
        ballPos = -1
        barPos = -1
        for x in range(len(self.screen)):
            for y in range(len(self.screen[x])):
                if self.screen[x][y] == 4:
                    ballPos = y
                elif self.screen[x][y] == 3:
                    barPos = y
                if barPos != -1 and ballPos != -1:
                    break
            if barPos != -1 and ballPos != -1:
                break

        if barPos == ballPos:
            return 0
        elif barPos > ballPos:
            return -1
        else:
            return 1

    def runGame(self, autoRun=True, showFrames=False):
        nextMove = None
        if autoRun:
            nextMove = self.getNextMove()
        else:
            self.printScreen()
        if autoRun and showFrames:
            self.printScreen()
            input()

        compResult = np.array(self.comp.run(nextMove, False)).reshape(-1, 3)

        while len(compResult) != 0:
            self.updateScreen(compResult)
            if autoRun:
                nextMove = self.getNextMove()
            else:
                self.printScreen()
            if autoRun and showFrames:
                self.printScreen()
                input()
            compResult = np.array(self.comp.run(nextMove, False)).reshape(-1, 3)
        return self.score

    def printScreen(self):
        print(self.score)
        for x in range(len(self.screen)):
            rowStr = ""
            for y in range(len(self.screen[x])):
                if self.screen[x][y] == 0:
                    rowStr += " "
                elif self.screen[x][y] == 1:
                    rowStr += "X"
                elif self.screen[x][y] == 2:
                    rowStr += "#"
                elif self.screen[x][y] == 3:
                    rowStr += "_"
                elif self.screen[x][y] == 4:
                    rowStr += "O"
            print(rowStr)


def part1(data, test=False) -> str:
    comp = IntcodeComputer(data[0].split(","))
    tiles = np.array(comp.run(None, False)).reshape(-1, 3)
    result = 0
    for t in tiles:
        if t[2] == 2:
            result += 1
    return str(result)


def part2(data, test=False) -> str:
    gameScreen = GameScreen(data[0].split(","), True)
    return gameScreen.runGame()
