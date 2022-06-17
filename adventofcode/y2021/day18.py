import math
import random


class SnailNum:
    def __init__(self, data, depth=0, parent=None):
        self.randID = random.randint(1, 10000)
        self.left = None
        self.leftIsNum = None
        self.right = None
        self.rightIsNum = None
        self.depth = depth
        self.parentSnailNum = parent

        data = data[1:-1]
        rightStart = data.find(",", 1)
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
            rightStart = data.find(",", nextClose)
            self.left = SnailNum(data[0 : nextClose + 1], depth + 1, self)
            self.leftIsNum = False
        else:
            self.left = int(data[0:rightStart])
            self.leftIsNum = True

        if data[rightStart + 1] == "[":
            openPos = rightStart + 2
            closePos = rightStart + 2
            nextOpen = data.find("[", openPos)
            nextClose = data.find("]", closePos)
            while not (nextOpen == -1 or nextOpen > nextClose):
                openPos = nextOpen + 1
                closePos = nextClose + 1
                nextOpen = data.find("[", openPos)
                nextClose = data.find("]", closePos)
            self.right = SnailNum(data[rightStart + 1 : nextClose + 1], depth + 1, self)
            self.rightIsNum = False
        else:
            self.right = int(data[rightStart + 1 :])
            self.rightIsNum = True

        pass

    def addition(self, snailNum):
        return SnailNum(
            "[" + self.printNum(False) + "," + snailNum.printNum(False) + "]"
        )

    def addLeft(self, amount, sameSide=True, goingUp=False):
        if self.leftIsNum:
            self.left += amount
        else:
            if goingUp:
                self.left.addLeft(amount, sameSide, goingUp)
            elif self.depth != 0 and sameSide:
                newSameSide = (
                    not self.parentSnailNum.leftIsNum
                ) and self.parentSnailNum.left.randID == self.randID

                self.parentSnailNum.addLeft(amount, newSameSide)
            elif self.depth == 0 and sameSide:
                pass
            else:
                self.left.addRight(amount, True, True)

    def addRight(self, amount, sameSide=True, goingUp=False):
        if self.rightIsNum:
            self.right += amount
        else:
            if goingUp:
                self.right.addRight(amount, sameSide, goingUp)
            elif self.depth != 0 and sameSide:
                newSameSide = (
                    not self.parentSnailNum.rightIsNum
                ) and self.parentSnailNum.right.randID == self.randID
                self.parentSnailNum.addRight(amount, newSameSide)
            elif self.depth == 0 and sameSide:
                pass
            else:
                self.right.addLeft(amount, True, True)

    def reduce(self):
        step = 0
        while True:
            step += 1

            if self.expload()[0]:
                continue

            if self.split():
                continue

            break

    def expload(self, hasExploaded=False):
        if not self.leftIsNum:
            hasExploaded, leftExploaded = self.left.expload(hasExploaded)
            if leftExploaded != None:
                self.addLeft(leftExploaded[0])
                self.addRight(leftExploaded[1], False)
                self.leftIsNum = True
                self.left = 0

        if not self.rightIsNum:
            hasExploaded, rightExploaded = self.right.expload(hasExploaded)
            if rightExploaded != None:
                self.addLeft(rightExploaded[0], False)
                self.addRight(rightExploaded[1])
                self.rightIsNum = True
                self.right = 0

        if not hasExploaded and self.depth >= 4:
            return (True, (self.left, self.right))

        return (hasExploaded, None)

    def split(self, didSplit=False):
        if not didSplit and self.leftIsNum and self.left >= 10:
            self.leftIsNum = False
            self.left = SnailNum(
                "["
                + str(math.floor(self.left / 2))
                + ","
                + str(math.ceil(self.left / 2))
                + "]"
            )
            self.left.depth = self.depth + 1
            self.left.parentSnailNum = self
            didSplit = True
        elif not didSplit and not self.leftIsNum:
            didSplit = self.left.split(didSplit)

        if not didSplit and self.rightIsNum and self.right >= 10:
            self.rightIsNum = False
            self.right = SnailNum(
                "["
                + str(math.floor(self.right / 2))
                + ","
                + str(math.ceil(self.right / 2))
                + "]"
            )
            self.right.depth = self.depth + 1
            self.right.parentSnailNum = self
            didSplit = True
        elif not didSplit and not self.rightIsNum:
            didSplit = self.right.split(didSplit)

        return didSplit

    def getMagnitude(self):
        rightNum = 0
        leftNum = 0
        if self.leftIsNum:
            leftNum = self.left
        else:
            leftNum = self.left.getMagnitude()

        if self.rightIsNum:
            rightNum = self.right
        else:
            rightNum = self.right.getMagnitude()

        return (3 * leftNum) + (2 * rightNum)

    def printNum(self, printStr=True):
        outStr = "["
        if self.leftIsNum:
            outStr += str(self.left)
        else:
            outStr += self.left.printNum(False)

        outStr += ","

        if self.rightIsNum:
            outStr += str(self.right)
        else:
            outStr += self.right.printNum(False)
        outStr += "]"

        if printStr:
            print(outStr)
        return outStr


def part1(data, test=False) -> str:
    result = SnailNum(data[0])

    for i in range(1, len(data)):
        result = result.addition(SnailNum(data[i]))
        result.reduce()
    result.reduce()

    return result.getMagnitude()


def part2(data, test=False) -> str:
    result = 0
    for x in range(len(data)):
        for y in range(len(data)):
            newCheck = SnailNum(data[x])
            newCheck = newCheck.addition(SnailNum(data[y]))
            newCheck.reduce()
            result = max(result, newCheck.getMagnitude())

            swapCheck = SnailNum(data[y])
            swapCheck = swapCheck.addition(SnailNum(data[x]))
            swapCheck.reduce()
            result = max(result, swapCheck.getMagnitude())

    return result
