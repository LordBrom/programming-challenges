import math


class SnailNum():
    def __init__(self, data, depth=0, parent=None):
        self.first = None
        self.firstIsNum = None
        self.last = None
        self.lastIsNum = None
        self.depth = depth
        self.parentSnailNum = parent

        data = data[1:-1]
        lastStart = 1
        if data[0] == "[":
            openPos = 1
            closePos = 1
            nextOpen = data.find("[", openPos)
            nextClose = data.find("]", closePos)
            while not (nextOpen == -1 or nextOpen > nextClose):
                openPos = nextOpen + 1
                closePos = nextClose + 1
                nextOpen = data.find("[", openPos)
                nextClose = data.find("]", closePos)
            lastStart = nextClose + 1
            self.first = SnailNum(data[0:nextClose + 1], depth + 1, self)
            self.firstIsNum = False
        else:
            self.first = int(data[0])
            self.firstIsNum = True

        if data[lastStart + 1] == "[":
            openPos = lastStart + 2
            closePos = lastStart + 2
            nextOpen = data.find("[", openPos)
            nextClose = data.find("]", closePos)
            while not (nextOpen == -1 or nextOpen > nextClose):
                openPos = nextOpen + 1
                closePos = nextClose + 1
                nextOpen = data.find("[", openPos)
                nextClose = data.find("]", closePos)
            self.last = SnailNum(
                data[lastStart + 1:nextClose + 1], depth + 1, self)
            self.lastIsNum = False
        else:
            self.last = int(data[lastStart + 1])
            self.lastIsNum = True

        pass

    def addition(self, snailNum):
        return SnailNum('[' + self.printNum(False) + ',' + snailNum.printNum(False) + ']')

    def addFirst(self, amount):
        if self.firstIsNum:
            self.first += amount
        else:
            self.first.addFirst(amount)

    def addLast(self, amount):
        if self.lastIsNum:
            self.last += amount
        else:
            self.last.addLast(amount)

    def reduce(self):
        if not self.firstIsNum:
            exp = self.first.reduce()
            if exp != None and exp[1] != 0:
                self.addLast(exp[1])
                self.firstIsNum = True
                self.first = 0
                return (exp[0], 0)

        if not self.lastIsNum:
            exp = self.last.reduce()
            if exp != None and exp[0] != 0:
                self.addFirst(exp[0])
                self.lastIsNum = True
                self.last = 0
                return (0, exp[1])

        if self.depth >= 4:
            firstResult = 0
            lastResult = 0
            if self.firstIsNum:
                firstResult = self.first
            else:
                pass

            return (firstResult, lastResult)

    def split(self):
        if self.firstIsNum and self.first >= 10:
            self.firstIsNum = False
            self.first = SnailNum(
                "[" + str(math.floor(self.first / 2)) + "," + str(math.floor(self.first / 2)) + "]")
        if self.lastIsNum and self.last >= 10:
            self.lastIsNum = False
            self.last = SnailNum(
                "[" + str(math.floor(self.last / 2)) + "," + str(math.floor(self.last / 2)) + "]")

    def printNum(self, printStr=True):
        outStr = "["
        if self.firstIsNum:
            outStr += str(self.first)
        else:
            outStr += self.first.printNum(False)

        outStr += ","

        if self.lastIsNum:
            outStr += str(self.last)
        else:
            outStr += self.last.printNum(False)
        outStr += "]"

        if printStr:
            print(outStr)
        return outStr


def part1(data):
    result = SnailNum(data[0])
    for i in range(1, len(data)):
        result.printNum()
        result = result.addition(SnailNum(data[i]))
        result.printNum()
        result.reduce()
    result.reduce()
    result.printNum()


def part2(data):
    return "not implemented"
