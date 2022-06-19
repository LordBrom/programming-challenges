import re
from typing import List

RE_STR = "Step ([A-Z]) must be finished before step ([A-Z]) can begin."


class Point:
    def __init__(self, name) -> None:
        self.name = name
        self.before: List[Point] = []
        self.after: List[Point] = []

    def __str__(self) -> str:
        result = "Step " + self.name + " must be finished before step(s) "
        first = True
        for p in self.after:
            if not first:
                result += ", "
            first = False
            result += p.name

        result += " can begin, and after "
        first = True
        for p in self.before:
            if not first:
                result += ", "
            first = False
            result += p.name

        result += " have begin."
        return result

    def addBeforePoint(self, beforePoint):
        self.before.append(beforePoint)

    def addAfterPoint(self, afterPoint):
        self.after.append(afterPoint)

    def canBeAdded(self, result):
        for p in self.before:
            if not p.name in result:
                return False
        return True


class Worker:
    def __init__(self, extraTime=60) -> None:
        self.workingOn = "."
        self.progress = 0
        self.extraTime = extraTime

    def __str__(self) -> str:
        return self.workingOn

    def startWorking(self, letter):
        if self.workingOn != ".":
            return False
        self.workingOn = letter
        self.progress = (ord(letter) - 64) + self.extraTime
        return True

    def tickSecond(self):
        if self.workingOn == ".":
            return None
        self.progress -= 1
        if self.progress == 0:
            result = self.workingOn.upper()
            self.workingOn = "."
            return result


def parsePointList(data):
    pointList = {}
    for d in data:
        reResult = re.search(RE_STR, d)
        thisPoint = reResult.group(1)
        afterPoint = reResult.group(2)

        if not thisPoint in pointList:
            pointList[thisPoint] = Point(thisPoint)
        if not afterPoint in pointList:
            pointList[afterPoint] = Point(afterPoint)
        pointList[afterPoint].addBeforePoint(pointList[thisPoint])
        pointList[thisPoint].addAfterPoint(pointList[afterPoint])
    return pointList


def part1(data, test=False):
    pointList = parsePointList(data)

    result = ""
    while len(result) < len(pointList):
        available = []
        for p in pointList:
            if not p in result and pointList[p].canBeAdded(result):
                available.append(p)
        available.sort()
        result += available[0]

    return result


def part2(data, test=False) -> str:
    pointList = parsePointList(data)
    workerCount = 5
    workers = []
    for i in range(workerCount):
        workers.append(Worker())

    second = 0
    result = ""
    beingWorked = ""
    while len(result) < len(pointList):
        for w in workers:
            addLetter = w.tickSecond()
            if addLetter != None:
                result += addLetter

        available = []
        for p in pointList:
            if not p in beingWorked and pointList[p].canBeAdded(result):
                available.append(p)
        available.sort()
        nextIndex = 0

        for w in workers:
            if len(available) <= nextIndex:
                break
            newWork = w.startWorking(available[nextIndex])
            if newWork:
                beingWorked += available[nextIndex]
                nextIndex += 1

        outStr = "sec: " + str(second)
        for i in range(len(workers)):
            outStr += " w" + str(i) + ": " + str(workers[i])
        outStr += " result: " + result

        # print(outStr)
        # input()
        second += 1

    return str(second - 1)
