import re

RE_STR = "(on|off) x=([-0-9]+)..([-0-9]+),y=([-0-9]+)..([-0-9]+),z=([-0-9]+)..([-0-9]+)"


class Cuboid:
    def __init__(self, xRange, yRange, zRange) -> None:
        self.xRange = xRange
        self.yRange = yRange
        self.zRange = zRange

    def __str__(self) -> str:
        result = ""
        result += str(self.xRange) + " "
        result += str(self.yRange) + " "
        result += str(self.zRange) + " "
        result += ": " + str(self.cubeSize()) + " cubes"
        return result

    def checkOverlap(self, other: "Cuboid"):
        if self.xRange[0] > other.xRange[1] or self.xRange[1] < other.xRange[0]:
            return None
        if self.yRange[0] > other.yRange[1] or self.yRange[1] < other.yRange[0]:
            return None
        if self.zRange[0] > other.zRange[1] or self.zRange[1] < other.zRange[0]:
            return None

        xRange = [
            max(self.xRange[0], other.xRange[0]),
            min(self.xRange[1], other.xRange[1]),
        ]
        yRange = [
            max(self.yRange[0], other.yRange[0]),
            min(self.yRange[1], other.yRange[1]),
        ]
        zRange = [
            max(self.zRange[0], other.zRange[0]),
            min(self.zRange[1], other.zRange[1]),
        ]

        return [xRange, yRange, zRange]

    def cubeSize(self):
        xDiff = self.xRange[1] - self.xRange[0] + 1
        yDiff = self.yRange[1] - self.yRange[0] + 1
        zDiff = self.zRange[1] - self.zRange[0] + 1
        return xDiff * yDiff * zDiff

    def isValid(self):
        return (
            self.xRange[0] <= self.xRange[1]
            and self.yRange[0] <= self.yRange[1]
            and self.zRange[0] <= self.zRange[1]
        )


def splitCube(cube1: "Cuboid", cube2: "Cuboid"):
    overlap = cube1.checkOverlap(cube2)
    if overlap == None:
        return [cube1]

    result = []
    result.append(
        Cuboid(cube1.xRange, cube1.yRange, [cube1.zRange[0], overlap[2][0] - 1])
    )
    result.append(
        Cuboid(cube1.xRange, cube1.yRange, [overlap[2][1] + 1, cube1.zRange[1]])
    )
    result.append(
        Cuboid([cube1.xRange[0], overlap[0][0] - 1], cube1.yRange, overlap[2])
    )
    result.append(
        Cuboid([overlap[0][1] + 1, cube1.xRange[1]], cube1.yRange, overlap[2])
    )
    result.append(Cuboid(overlap[0], [cube1.yRange[0], overlap[1][0] - 1], overlap[2]))
    result.append(Cuboid(overlap[0], [overlap[1][1] + 1, cube1.yRange[1]], overlap[2]))

    return [cube for cube in result if cube.isValid()]


def part1(data, test=False) -> str:
    reactor = {}
    for d in data:
        reResult = re.search(RE_STR, d)
        for x in range(int(reResult.group(2)), int(reResult.group(3)) + 1):
            if not (-50 <= x <= 50):
                continue
            for y in range(int(reResult.group(4)), int(reResult.group(5)) + 1):
                if not (-50 <= y <= 50):
                    continue
                for z in range(int(reResult.group(6)), int(reResult.group(7)) + 1):
                    if not (-50 <= z <= 50):
                        continue
                    posStr = str(x) + "_" + str(y) + "_" + str(z)
                    if reResult.group(1) == "on":
                        reactor[posStr] = True
                    else:
                        if posStr in reactor:
                            reactor.pop(posStr)

    return str(len(reactor))


def part2(data, test=False) -> str:
    cubes = []
    for d in data:
        reResult = re.search(RE_STR, d)
        toggle = reResult.group(1) == "on"
        xRange = [int(reResult.group(2)), int(reResult.group(3))]
        yRange = [int(reResult.group(4)), int(reResult.group(5))]
        zRange = [int(reResult.group(6)), int(reResult.group(7))]
        newCube = Cuboid(xRange, yRange, zRange)

        newCubes = []
        for cube in cubes:
            newCubes.extend(splitCube(cube, newCube))
        if toggle:
            newCubes.append(newCube)
        cubes = newCubes

    result = 0
    for cube in cubes:
        result += cube.cubeSize()

    return str(result)
