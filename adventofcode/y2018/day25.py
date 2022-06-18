from aoc import manhattan_distance


class Constellation:
    def __init__(self, id, startStar, distance=3) -> None:
        self.id = id
        self.stars = [startStar]
        self.distance = distance

    def __str__(self) -> str:
        result = "\n"
        for star in self.stars:
            result += "\n" + str(star)
        return result

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Constellation):
            return False
        return __o.id == self.id

    def checkStar(self, newStar):
        for star in self.stars:
            if manhattan_distance(star, newStar) <= self.distance:
                return True
        return False

    def checkConstellation(self, other: "Constellation"):
        for otherStar in other.stars:
            if self.checkStar(otherStar):
                return True
        return False

    def addStar(self, newStar):
        self.stars.append(newStar)

    def mergeConstellations(self, other: "Constellation"):
        for otherStar in other.stars:
            self.addStar(otherStar)


def parseInput(data):
    stars = []

    for d in data:
        stars.append([int(p) for p in d.split(",")])

    return stars


def part1(data, test=False) -> str:
    stars = parseInput(data)
    count = 0
    constellations = []
    for star in stars:
        merged = False
        for constellation in constellations:
            if constellation.checkStar(star):
                merged = True
                constellation.addStar(star)
                break
        if not merged:
            constellations.append(Constellation(count, star))
            count += 1

    foundOne = True
    while foundOne:
        foundOne = False
        for outerCheck in range(len(constellations)):
            if constellations[outerCheck] == None:
                continue
            for innerCheck in range(len(constellations)):
                if constellations[innerCheck] == None:
                    continue
                if outerCheck == innerCheck:
                    continue
                if constellations[outerCheck].checkConstellation(
                    constellations[innerCheck]
                ):
                    foundOne = True
                    constellations[outerCheck].mergeConstellations(
                        constellations[innerCheck]
                    )
                    constellations[innerCheck] = None

    result = 0
    for constellation in constellations:
        if constellation != None:
            result += 1

    return str(result)


def part2(data, test=False) -> str:
    return "Merry Christmas!"
