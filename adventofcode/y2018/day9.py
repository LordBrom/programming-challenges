import typing
import re

RE_STR = "([0-9]+) players; last marble is worth ([0-9]+) points"


class Marble:
    def __init__(self, value) -> None:
        self.value = value
        self.left: typing.Optional[Marble] = None
        self.right: typing.Optional[Marble] = None

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Marble) and self.value == __o.value

    def getClockWise(self, count):
        if count == 0:
            return self
        return self.right.getClockWise(count - 1)

    def getCounterClockWise(self, count):
        if count == 0:
            return self
        return self.left.getCounterClockWise(count - 1)

    def removeSelf(self):
        self.right.left = self.left
        self.left.right = self.right
        return self.getClockWise(1)


class MarbleGame:
    def __init__(self, players, marbles) -> None:
        self.players = players
        self.marbles = marbles
        self.marbleValue = 1
        self.currentPlayer = 0
        self.playerScores = [0 for x in range(self.players)]

        self.startMarble = Marble(0)
        self.startMarble.left = self.startMarble
        self.startMarble.right = self.startMarble
        self.activeMarble = self.startMarble

    def __str__(self) -> str:
        if self.marbleValue == 1:
            result = "[-] "
        else:
            result = "[" + str(self.currentPlayer) + "] "

        printMarble = self.startMarble
        if printMarble == self.activeMarble:
            result += " (" + str(printMarble.value) + ")"
        else:
            result += " " + str(printMarble.value)

        while printMarble.getClockWise(1) != self.startMarble:
            printMarble = printMarble.getClockWise(1)
            if printMarble == self.activeMarble:
                result += " (" + str(printMarble.value) + ")"
            else:
                result += " " + str(printMarble.value)
        return result

    def takeTurn(self):
        if self.marbleValue % 23 == 0:
            self.addScore(self.marbleValue)
            self.activeMarble = self.activeMarble.getCounterClockWise(7)
            self.addScore(self.activeMarble.value)
            self.activeMarble = self.activeMarble.removeSelf()
        else:
            cw1 = self.activeMarble.getClockWise(1)
            cw2 = self.activeMarble.getClockWise(2)
            self.activeMarble = Marble(self.marbleValue)
            cw1.right = self.activeMarble
            cw2.left = self.activeMarble
            self.activeMarble.left = cw1
            self.activeMarble.right = cw2
        self.marbleValue += 1
        self.nextPlayer()

    def nextPlayer(self):
        self.currentPlayer += 1
        self.currentPlayer %= self.players

    def addScore(self, amount):
        self.playerScores[self.currentPlayer] += amount

    def runGame(self):
        for i in range(self.marbles):
            self.takeTurn()
        return self.getWinner()[0]

    def getWinner(self):
        bestPos = 0
        for i in range(len(self.playerScores)):
            if self.playerScores[i] > self.playerScores[bestPos]:
                bestPos = i
        return self.playerScores[bestPos], bestPos


def parseInput(data):
    reResult = re.search(RE_STR, data)
    return (int(reResult.group(1)), int(reResult.group(2)))


def part1(data, test=False) -> str:
    data = data[0]
    playerCount, marbleCount = parseInput(data)
    marbleGame = MarbleGame(playerCount, marbleCount)
    return str(marbleGame.runGame())


def part2(data, test=False) -> str:
    data = data[0]
    playerCount, marbleCount = parseInput(data)
    marbleGame = MarbleGame(playerCount, marbleCount * 100)
    return str(marbleGame.runGame())
