import re
from functools import lru_cache

RE_STR = "Player ([0-9]) starting position: ([0-9])"


def nextDie100Value(dieValue):
    next = dieValue
    dieValue += 1
    if dieValue > 100:
        dieValue = 1
    return next, dieValue


class Game:
    def __init__(self, player1Pos, player2Pos, winningScore) -> None:
        self.playerPosition = [player1Pos - 1, player2Pos - 1]
        self.playerScore = [0, 0]
        self.winningScore = winningScore

    def __str__(self) -> str:
        result = (
            "Player 1 at "
            + str(self.playerPosition[0])
            + " with score: "
            + str(self.playerScore[0])
        )
        result += (
            "\nPlayer 2 at "
            + str(self.playerPosition[1])
            + " with score: "
            + str(self.playerScore[1])
        )
        return result

    def movePiece(self, player, spaces):
        self.playerPosition[player] += spaces
        self.playerPosition[player] = self.playerPosition[player] % 10
        self.playerScore[player] += self.playerPosition[player] + 1

        if self.playerScore[player] >= self.winningScore:
            return True

        return False


def part1(data, test=False) -> str:
    p1Result = re.search(RE_STR, data[0])
    p2Result = re.search(RE_STR, data[1])
    game = Game(int(p1Result.group(2)), int(p2Result.group(2)), 1000)

    dieValue = 1
    run = True
    player = 0
    dieRolls = 0
    while run:
        die1, dieValue = nextDie100Value(dieValue)
        die2, dieValue = nextDie100Value(dieValue)
        die3, dieValue = nextDie100Value(dieValue)
        dieRolls += 3
        spaces = die1 + die2 + die3

        run = not game.movePiece(player, spaces)
        player += 1
        player = player % 2

    return str(min(game.playerScore[0], game.playerScore[1]) * dieRolls)


@lru_cache(maxsize=None)
def runGame(p1, p2, s1=0, s2=0, player=0):
    wins = [0, 0]
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                if player == 0:
                    nextP1 = p1 + d1 + d2 + d3
                    if nextP1 > 10:
                        nextP1 -= 10
                    nextS1 = s1 + nextP1
                    if nextS1 >= 21:
                        wins[player] += 1
                    else:
                        subWins = runGame(nextP1, p2, nextS1, s2, 1)
                        wins[0] += subWins[0]
                        wins[1] += subWins[1]

                else:
                    nextP2 = p2 + d1 + d2 + d3
                    if nextP2 > 10:
                        nextP2 -= 10
                    nextS2 = s2 + nextP2
                    if nextS2 >= 21:
                        wins[player] += 1
                    else:
                        subWins = runGame(p1, nextP2, s1, nextS2, 0)
                        wins[0] += subWins[0]
                        wins[1] += subWins[1]

    return wins


def part2(data, test=False) -> str:
    p1Result = re.search(RE_STR, data[0])
    p2Result = re.search(RE_STR, data[1])
    result = runGame(int(p1Result.group(2)), int(p2Result.group(2)))
    return str(max(result[0], result[1]))
