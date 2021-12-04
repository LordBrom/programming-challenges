import re


class BingoBoard:
    def __init__(self, nums):
        self.board = []
        for x in range(5):
            self.board.append([[0, False] for y in range(5)])

        for x in range(5):
            reResults = re.search(
                "[ ]?([0-9]+)[ ]+([0-9]+)[ ]+([0-9]+)[ ]+([0-9]+)[ ]+([0-9]+)",  nums[x])
            for y in range(5):
                self.board[x][y][0] = reResults.group(y + 1)

    def check_num(self, num):
        for x in range(5):
            for y in range(5):
                if self.board[x][y][0] == num:
                    self.board[x][y][1] = True
                    return

    def check_win(self):
        for x in range(5):
            cnt = 0
            for y in range(5):
                if self.board[x][y][1]:
                    cnt += 1
            if cnt == 5:
                return True

        for x in range(5):
            cnt = 0
            for y in range(5):
                if self.board[y][x][1]:
                    cnt += 1
            if cnt == 5:
                return True
        return False

    def count_unchecked(self):
        total = 0
        for x in range(5):
            for y in range(5):
                if not self.board[x][y][1]:
                    total += int(self.board[x][y][0])
        return total

    def print_board(self):
        print("")
        print("")
        for x in range(5):
            rowStr = ""
            for y in range(5):
                if self.board[x][y][1]:
                    rowStr += "X" + self.board[x][y][0] + " "
                else:
                    rowStr += "_" + self.board[x][y][0] + " "
            print(rowStr)
        print("")
        print("")


def parseInput(input):
    result = []
    result.append(input[0].split(","))
    input.pop(0)
    input.pop(0)

    result.append([])

    i = 0
    while i < len(input):
        newBoard = []
        for x in range(i, i+5):
            newBoard.append(input[x])
        result[1].append(BingoBoard(newBoard))
        i += 6

    return result


def part1(input):
    parsedInput = parseInput(input)
    selectedNums = parsedInput[0]
    boards = parsedInput[1]

    for i in selectedNums:
        for b in boards:
            b.check_num(i)
            if b.check_win():
                return int(i) * b.count_unchecked()
    return "not found"


def part2(input):
    parsedInput = parseInput(input)
    selectedNums = parsedInput[0]
    boards = parsedInput[1]

    wonBoard = []

    for i in selectedNums:
        for b in range(len(boards)):
            if b in wonBoard:
                continue
            boards[b].check_num(i)
            if boards[b].check_win():
                wonBoard.append(b)
                if len(wonBoard) == len(boards):
                    return int(i) * boards[b].count_unchecked()
    return "not found"
