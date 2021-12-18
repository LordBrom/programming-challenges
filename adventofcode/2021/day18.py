import math
import random


class SnailNum():
    def __init__(self, data, depth=0, parent=None):
        self.randID = random.randint(1, 10000)
        self.first = None
        self.firstIsNum = None
        self.last = None
        self.lastIsNum = None
        self.depth = depth
        self.parentSnailNum = parent

        data = data[1:-1]
        lastStart = data.find(",", 1)
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
            lastStart = data.find(",", nextClose)
            self.first = SnailNum(data[0:nextClose + 1], depth + 1, self)
            self.firstIsNum = False
        else:
            # print(data[0:lastStart])
            self.first = int(data[0:lastStart])
            self.firstIsNum = True

        lastEnd = data.find("]", lastStart)
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
            # print(data[lastStart + 1:])
            self.last = int(data[lastStart + 1:])
            self.lastIsNum = True

        pass

    def addition(self, snailNum):
        return SnailNum('[' + self.printNum(False) + ',' + snailNum.printNum(False) + ']')

    def addFirst(self, amount, sameSide=True, goingUp=False):
        if self.firstIsNum:
            self.first += amount
        else:
            if goingUp:
                self.first.addFirst(amount, sameSide, goingUp)
            elif self.depth != 0 and sameSide:
                newSameSide = (
                    not self.parentSnailNum.firstIsNum) and self.parentSnailNum.first.randID == self.randID

                self.parentSnailNum.addFirst(
                    amount, newSameSide)
            elif self.depth == 0:
                pass
            else:
                self.first.addLast(
                    amount, True, True)

    def addLast(self, amount, sameSide=True, goingUp=False):
        if self.lastIsNum:
            self.last += amount
        else:
            if goingUp:
                self.last.addLast(amount, sameSide, goingUp)
            elif self.depth != 0 and sameSide:
                newSameSide = (
                    not self.parentSnailNum.lastIsNum) and self.parentSnailNum.last.randID == self.randID
                self.parentSnailNum.addLast(
                    amount, newSameSide)
            elif self.depth == 0:
                pass
            else:
                self.last.addFirst(
                    amount, True, True)

    def reduce(self):
        current = self.printNum(False)
        last = ""
        step = 0
        while True:
            self.printNum()
            step += 1
            last = current
            self.expload()
            current = self.printNum(False)

            if last != current:
                continue

            last = current
            self.split()
            # print("before", last)
            current = self.printNum(False)

            if last == current:
                break

    def expload(self):
        if not self.firstIsNum:
            firstExploaded = self.first.expload()
            if firstExploaded != None:
                self.addLast(firstExploaded[1], False)
                self.addFirst(firstExploaded[0])
                self.firstIsNum = True
                self.first = 0

        if not self.lastIsNum:
            lastExploaded = self.last.expload()
            if lastExploaded != None:
                self.addLast(lastExploaded[1])
                self.addFirst(lastExploaded[0], False)
                self.lastIsNum = True
                self.last = 0

        if self.depth >= 4:
            return (self.first, self.last)

    def split(self):
        didSplit = False
        if not didSplit and self.firstIsNum and self.first >= 10:
            self.firstIsNum = False
            self.first = SnailNum(
                "[" + str(math.floor(self.first / 2)) + "," + str(math.ceil(self.first / 2)) + "]")
            self.first.depth = self.depth + 1
            self.first.parentSnailNum = self
            didSplit = True
        elif not didSplit and not self.firstIsNum:
            didSplit = self.first.split()

        if not didSplit and self.lastIsNum and self.last >= 10:
            self.lastIsNum = False
            self.last = SnailNum(
                "[" + str(math.floor(self.last / 2)) + "," + str(math.ceil(self.last / 2)) + "]")
            self.last.depth = self.depth + 1
            self.last.parentSnailNum = self
            didSplit = True
        elif not didSplit and not self.lastIsNum:
            didSplit = self.last.split()
        return didSplit

    def getMagnitude(self):
        lastNum = 0
        firstNum = 0
        if self.firstIsNum:
            firstNum = self.first
        else:
            firstNum = self.first.getMagnitude()

        if self.lastIsNum:
            lastNum = self.last
        else:
            lastNum = self.last.getMagnitude()

        return (3 * firstNum) + (2 * lastNum)

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
        startNum = result.printNum(False)
        newNum = SnailNum(data[i])
        result = result.addition(SnailNum(data[i]))
        result.reduce()
        print(startNum, " + ", newNum.printNum(False),
              " = ", result.printNum(False))

    return result.getMagnitude()


def part2(data):
    return "not implemented"
