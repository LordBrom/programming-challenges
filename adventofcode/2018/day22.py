import sys
import heapq
from enum import Enum


class CaveType(Enum):
    ROCKY = 0
    WET = 1
    NARROW = 2


class Gear(Enum):
    NEITHER = 0
    TORCH = 1
    CLIMBING = 2


TYPE_STR = {
    CaveType.ROCKY: ".",
    CaveType.WET: "=",
    CaveType.NARROW: "|"}

ALLOWED_GEAR = {
    CaveType.ROCKY: [Gear.TORCH, Gear.CLIMBING],
    CaveType.WET: [Gear.CLIMBING, Gear.NEITHER],
    CaveType.NARROW: [Gear.NEITHER, Gear.TORCH]}


class Cave():
    def __init__(self, x, y, depth, target, upCave, leftCave) -> None:
        self.x = x
        self.y = y
        self.target = target
        self.upCave = upCave
        self.leftCave = leftCave
        self.depth = depth
        self.erosionLevel = None
        self.geologicIndex = None
        self.type = None
        self.distance = sys.maxsize
        self.gear = None
        self.gearOptions = None
        self.cameFromCave = None
        self.isTarget = False

    def setGeoData(self):
        if [self.x, self.y] == self.target:
            self.upCave.getErosionLevel()
            self.leftCave.getErosionLevel()
            self.geologicIndex = 0
            self.isTarget = True
        else:
            if self.x == 0:
                if self.y == 0:
                    self.geologicIndex = 0
                self.geologicIndex = self.y * 48271
            elif self.y == 0:
                self.geologicIndex = self.x * 16807
            else:
                self.geologicIndex = self.upCave.getErosionLevel() * self.leftCave.getErosionLevel()

        self.erosionLevel = (self.geologicIndex + self.depth) % 20183
        self.type = CaveType(self.erosionLevel % 3)

    def getErosionLevel(self):
        if self.erosionLevel == None:
            self.setGeoData()
        return self.erosionLevel

    def __eq__(self, __o: object) -> bool:
        if __o == None or __o.x == None or __o.y == None:
            return False
        return __o.x == self.x and __o.y == self.y

    def __lt__(self, __o: object) -> bool:
        if __o == None or __o.distance == None:
            return False
        return self.distance < __o.distance

    def __str__(self) -> str:
        if self.x == 0 and self.y == 0:
            return "{} MT    ".format(TYPE_STR[self.type])
        if self.isTarget:
            return "{}  T    ".format(TYPE_STR[self.type])
        if self.distance == sys.maxsize:
            return "{}--/    ".format(TYPE_STR[self.type])
        else:
            return "{}{:02d}{};{}/{}".format(TYPE_STR[self.type], self.distance, self.gear.name[0] if self.gear != None else "/", self.gearOptions[0].name[0] if self.gearOptions != None else "_", self.gearOptions[1].name[0] if self.gearOptions != None and len(self.gearOptions) == 2 else "_")


class CaveSystem():
    def __init__(self, depth, target) -> None:
        self.target = target
        self.depth = depth

        self.caves = []
        for x in range(depth):
            caveRow = []
            for y in range(depth):
                caveRow.append(
                    Cave(x, y, depth, target, self.caves[x-1][y] if x > 0 else None, caveRow[-1] if y > 0 else None))
            self.caves.append(caveRow)

        self.activeCave = None

    def __str__(self) -> str:
        result = ""
        for x in range(self.target[0] + 6):
            rowStr = ""
            for y in range(self.target[1] + 6):
                rowStr += str(self.caves[y][x])
                if [y, x] == self.activeCave:
                    rowStr += "X "
                else:
                    rowStr += "  "
            result += "\n" + rowStr
        return result

    def determineDanger(self):
        result = 0
        for x in range(self.target[0] + 1):
            for y in range(self.target[1] + 1):
                if self.caves[x][y].type == None:
                    self.caves[x][y].setGeoData()
                result += self.caves[x][y].type.value

        return result

    def followPath(self):
        gearSwapTime = 7

        visited = []
        caveQueue = []
        currentCave = self.caves[0][0]
        currentCave.distance = 0
        currentCave.gear = Gear.TORCH
        currentCave.gearOptions = [Gear.TORCH]
        caveQueue = [currentCave]
        # caveQueue.append(self.caves[0][0])
        self.activeCave = [currentCave.x, currentCave.y]

        while currentCave != self.caves[self.target[0]][self.target[1]]:
            for diffX in range(-1, 2):
                for diffY in range(-1, 2):
                    if diffX == 0 and diffY == 0 or diffX != 0 and diffY != 0:
                        continue

                    x = diffX + currentCave.x
                    y = diffY + currentCave.y
                    if x < 0 or y < 0 or x >= self.depth or y >= self.depth:
                        continue

                    newCave = self.caves[x][y]

                    if newCave.type == None:
                        newCave.setGeoData()

                    newDist = currentCave.distance + 1
                    if not ALLOWED_GEAR[newCave.type][0] in currentCave.gearOptions and not ALLOWED_GEAR[newCave.type][1] in currentCave.gearOptions:
                        newDist += gearSwapTime

                    if newDist < newCave.distance:
                        newCave.distance = newDist
                        newCave.cameFromCave = currentCave

                    if not newCave in visited and not newCave in caveQueue:
                        heapq.heappush(caveQueue, newCave)
                        caveQueue.append(newCave)
            caveQueue.remove(currentCave)
            visited.append(currentCave)

            currentCave = heapq.heappop(caveQueue)
            #currentCave = caveQueue[0]
            # for cave in caveQueue:
            #    if cave.distance < currentCave.distance:
            #        currentCave = cave

            prevGearOptions = currentCave.cameFromCave.gearOptions
            # 0 match
            if not ALLOWED_GEAR[currentCave.type][0] in prevGearOptions and not ALLOWED_GEAR[currentCave.type][1] in prevGearOptions:
                currentCave.gearOptions = ALLOWED_GEAR[currentCave.type]

            # 2 match; going to same type
            elif ALLOWED_GEAR[currentCave.type][0] in prevGearOptions and ALLOWED_GEAR[currentCave.type][1] in prevGearOptions:
                currentCave.gearOptions = prevGearOptions

            # 1 match
            elif not ALLOWED_GEAR[currentCave.type][0] in prevGearOptions or not ALLOWED_GEAR[currentCave.type][1] in prevGearOptions:
                if prevGearOptions[0] in ALLOWED_GEAR[currentCave.type]:
                    nextGear = prevGearOptions[0]
                elif prevGearOptions[1] in ALLOWED_GEAR[currentCave.type]:
                    nextGear = prevGearOptions[1]
                currentCave.gear = nextGear
                currentCave.gearOptions = [nextGear]

            # else?
            else:
                currentCave.gearOptions = prevGearOptions
            self.activeCave = [currentCave.x, currentCave.y]

        if not Gear.TORCH in currentCave.gearOptions:
            currentCave.distance += 7


def parseInput(data):
    depthSplit = data[0].split(" ")
    targetSplit = data[1].split(" ")
    depth = int(depthSplit[1])
    target = targetSplit[1].split(",")
    return depth, [int(target[0]), int(target[1])]


def part1(data):
    depth, target = parseInput(data)
    caveSystem = CaveSystem(depth, target)
    return caveSystem.determineDanger()


def part2(data):
    depth, target = parseInput(data)
    caveSystem = CaveSystem(depth, target)
    print('done1')
    # caveSystem.caves[target[0]][target[1]].setGeoData()
    # print('done2')
    caveSystem.followPath()
    return caveSystem.caves[target[0]][target[1]].distance
