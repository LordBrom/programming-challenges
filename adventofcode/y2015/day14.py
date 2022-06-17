import re
import math

RE_STR = "(.+) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds."


class Reindeer:
    def __init__(self, name, dist, time, rest) -> None:
        self.name = name
        self.flyDist = int(dist)
        self.flyTime = int(time)
        self.restTime = int(rest)
        self.raceDist = 0
        self.raceTime = 0

    def __str__(self) -> str:
        return "After {} seconds, {} has flown a total of {} km.".format(
            self.raceTime, self.name, self.raceDist
        )

    def __lt__(self, __o: object) -> bool:
        return self.raceDist < __o.raceDist

    def race(self, time=2503):
        raceTime = time
        resting = False
        while raceTime > 0:
            if resting:
                restTime = min(self.restTime, raceTime)
                raceTime -= restTime
                self.raceTime += restTime
                resting = False
            else:
                flyTime = min(self.flyTime, raceTime)
                self.raceDist += flyTime * self.flyDist
                raceTime -= flyTime
                self.raceTime += flyTime
                resting = True

    def raceStep(self, atTime):
        cycleLength = self.flyTime + self.restTime
        fullCycles = math.floor(atTime / cycleLength)
        result = fullCycles * self.flyTime * self.flyDist

        partialCycle = atTime % cycleLength
        result += min(self.flyTime, partialCycle) * self.flyDist

        return result


def parseInput(data):
    reindeer = []
    for d in data:
        reResult = re.search(RE_STR, d)
        reindeer.append(
            Reindeer(
                reResult.group(1),
                reResult.group(2),
                reResult.group(3),
                reResult.group(4),
            )
        )
    return reindeer


def part1(data, test=False) -> str:
    reindeer = parseInput(data)
    for r in reindeer:
        r.race()
    reindeer.sort()

    return reindeer[-1].raceDist


def part2(data, test=False) -> str:
    reindeer = parseInput(data)
    points = [0 for x in range(len(reindeer))]
    for i in range(2503):
        best = 0
        legWinners = []
        for r in range(len(reindeer)):
            check = reindeer[r].raceStep(i + 1)
            if check > best:
                best = check
                legWinners = [r]
            elif check == best:
                legWinners.append(r)
        for p in legWinners:
            points[p] += 1

    points.sort()
    return str(points[-1])
