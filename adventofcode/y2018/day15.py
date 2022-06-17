import numpy as np


class Unit:
    def __init__(self, team) -> None:
        self.team = team
        self.health = 200
        self.attack = 3

    def __str__(self) -> str:
        return self.team

    def moveTarget(self, otherTeam):
        pass


class Combat:
    def __init__(self, data) -> None:
        self.board = []
        self.team1 = []
        self.team2 = []
        for x in range(len(data)):
            boardRow = []
            for y in range(len(data[x])):
                if data[x][y] == "E":
                    newUnit = Unit(data[x][y])
                    boardRow.append(newUnit)
                    self.team1.append(newUnit)
                elif data[x][y] == "E":
                    newUnit = Unit(data[x][y])
                    boardRow.append(newUnit)
                    self.team2.append(newUnit)
                else:
                    boardRow.append(Unit(data[x][y]))
            self.board.append(boardRow)

    def __str__(self) -> str:
        result = ""
        for x in range(len(self.board)):
            rowStr = ""
            for y in range(len(self.board[x])):
                rowStr += str(self.board[x][y])
            result += "\n" + rowStr
        return result

    def doRound(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y] in ["#", "."]:
                    continue
        pass


def part1(data, test=False) -> str:
    combat = Combat(data)
    print(combat)
    return "not implemented"


def part2(data, test=False) -> str:
    return "not implemented"
