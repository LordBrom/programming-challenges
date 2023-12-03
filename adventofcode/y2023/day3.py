from aoc import get_neighbors
from typing import List

class Number():

    def __init__(self,num,pos) -> None:
        self.num = int(num)
        self.pos = pos

    def __str__(self) -> str:
        return str(self.num) + " at " + str(self.pos)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Number):
            return False

        for selfPoint in self.pos:
            for otherPoint in __o.pos:
                if selfPoint == otherPoint:
                    return True
        return False


def get_numbers(board):

    numbers: List[Number] = []
    for x,_ in enumerate(board):
        for y,_ in enumerate(board[x]):
            if board[x][y].isnumeric():
                if y > 0 and board[x][y - 1].isnumeric():
                    continue
                startPos = x
                endPos = y
                num = ""
                pos = set()
                while endPos < len(board) and board[startPos][endPos].isnumeric():
                    num += str(board[startPos][endPos])
                    pos.add((startPos,endPos))
                    endPos += 1

                newNum = Number(num, pos)
                numbers.append(newNum)

    return numbers


def part1(data, test=False) -> str:
    numbers: List[Number] = get_numbers(data)
    result = 0
    for x, row in enumerate(data):
        for y, col in enumerate(row):
            found: List[Number] = []
            if col.isnumeric() or col == ".":
                continue

            neighbors = get_neighbors(data, x, y, True)
            for neighbor in neighbors:
                if data[neighbor[0]][neighbor[1]].isnumeric():
                    number: Number
                    for number in numbers:
                        if (neighbor[0], neighbor[1]) in number.pos:
                            if not number in found:
                                result += number.num
                                found.append(number)
                            break
    return str(result)


def part2(data, test=False) -> str:
    numbers = get_numbers(data)
    result = 0
    for x, row in enumerate(data):
        for y, col in enumerate(row):
            if col != "*":
                continue

            found: List[Number] = []
            neighbors = get_neighbors(data, x, y, True)
            for neighbor in neighbors:
                if data[neighbor[0]][neighbor[1]].isnumeric():
                    number: Number
                    for number in numbers:
                        if (neighbor[0], neighbor[1]) in number.pos:
                            if not number in found:
                                found.append(number)
                            break
            if len(found) == 2:
                result += found[0].num * found[1].num
    return str(result)
