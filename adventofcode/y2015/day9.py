import sys
import re


class Location:
    def __init__(self, name) -> None:
        self.name = name
        self.distances = {}

    def __str__(self) -> str:
        return self.name

    def setDist(self, other, distance):
        self.distances[other] = distance

    def followPath(self, locations, visited=[], part1=True):
        visited.append(self.name)

        best = None

        for next in self.distances:
            if not next in visited:

                check = self.distances[next] + locations[next].followPath(
                    locations, visited.copy(), part1
                )

                if part1 and (best == None or check < best):
                    best = check
                elif not part1 and (best == None or check > best):
                    best = check

        if best == None:
            best = 0

        return best


def part1(data, test=False) -> str:
    reStr = "(.+) to (.+) = ([0-9]+)"
    locations = {}
    for d in data:
        reResult = re.search(reStr, d)
        loc1 = reResult.group(1)
        loc2 = reResult.group(2)
        dist = int(reResult.group(3))
        if not loc1 in locations:
            locations[loc1] = Location(loc1)
        if not loc2 in locations:
            locations[loc2] = Location(loc2)
        locations[loc1].setDist(loc2, dist)
        locations[loc2].setDist(loc1, dist)

    best = sys.maxsize
    for start in locations:
        check = locations[start].followPath(locations, [])
        if check < best:
            best = check

    return str(best)


def part2(data, test=False) -> str:
    reStr = "(.+) to (.+) = ([0-9]+)"
    locations = {}
    for d in data:
        reResult = re.search(reStr, d)
        loc1 = reResult.group(1)
        loc2 = reResult.group(2)
        dist = int(reResult.group(3))
        if not loc1 in locations:
            locations[loc1] = Location(loc1)
        if not loc2 in locations:
            locations[loc2] = Location(loc2)
        locations[loc1].setDist(loc2, dist)
        locations[loc2].setDist(loc1, dist)

    best = 0
    for start in locations:
        check = locations[start].followPath(locations, [], False)
        if check > best:
            best = check

    return str(best)
