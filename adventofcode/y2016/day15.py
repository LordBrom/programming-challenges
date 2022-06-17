from ast import parse
import re


class Disc():
    def __init__(self, num, count, pos) -> None:
        self.num = int(num)
        self.count = int(count)
        self.pos = int(pos)
        self.time = 0

    def __str__(self) -> str:
        return "Disc #{} has {} positions; at time={}, it is at position {}.".format(self.num, self.count, self.time, self.pos)

    def checkTime(self, time):
        return (self.pos + time) % self.count == 0


def parseInputs(data):
    discs = []
    reStr = "Disc #([0-9]+) has ([0-9]+) positions; at time=0, it is at position ([0-9]+)."
    for d in data:
        reRes = re.search(reStr, d)
        discs.append(Disc(reRes.group(1), reRes.group(2), reRes.group(3)))
    return discs


def dropBall(discs, time):
    fallTime = 0
    for disc in discs:
        fallTime += 1
        if not disc.checkTime(time + fallTime):
            return False
    return True


def part1(data):
    discs = parseInputs(data)
    time = 0
    while True:
        if dropBall(discs, time):
            return time
        time += 1
    return ""


def part2(data):
    discs = parseInputs(data)
    discs.append(Disc(len(discs), 11, 0))
    time = 0
    while True:
        if dropBall(discs, time):
            return time
        time += 1
    return ""
