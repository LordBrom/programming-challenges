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
        self.gearOptions = None
        self.cameFromCave = None
        self.isTarget = False
        self.geoSet = False

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
            return "{} M;T  ".format(TYPE_STR[self.type])
        if self.isTarget:
            return "{} DEST ".format(TYPE_STR[self.type])
        if self.distance == sys.maxsize:
            return "{}--    ".format(TYPE_STR[self.type])
        else:
            return "{}{:02d};{}/{}".format(TYPE_STR[self.type], self.distance, self.gearOptions[0].name[0] if self.gearOptions != None else "_", self.gearOptions[1].name[0] if self.gearOptions != None and len(self.gearOptions) == 2 else "_")

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
        self.geoSet = True

    def getErosionLevel(self):
        if not self.geoSet:
            self.setGeoData()
        return self.erosionLevel


class CaveSystem():
    def __init__(self, depth, target) -> None:
        self.target = target
        self.depth = depth
        self.activeCave = None

        self.caves = [[Cave(0, 0, depth, target, None, None)]]
        for x in range(target[0]):
            self.addCol()

        for y in range(target[1]):
            self.addRow()

    def __str__(self) -> str:
        result = ""
        for x in range(min(len(self.caves), self.target[0] + 6)):
            rowStr = ""
            for y in range(min(len(self.caves[x]), self.target[1] + 6)):
                if not self.caves[x][y].geoSet:
                    self.caves[x][y].setGeoData()
                rowStr += str(self.caves[x][y])
                if [x, y] == self.activeCave:
                    rowStr += "X "
                else:
                    rowStr += "  "
            result += "\n" + rowStr
        return result

    def addCol(self):
        y = len(self.caves[0])
        for x in range(len(self.caves)):

            upCave = None
            leftCave = None
            if x > 0:
                upCave = self.caves[x-1][y]
            if y > 0:
                leftCave = self.caves[x][y-1]

            self.caves[x].append(
                Cave(x, y, self.depth, self.target, upCave, leftCave))

    def addRow(self):
        x = len(self.caves)
        newRow = []
        for y in range(len(self.caves[0])):

            upCave = None
            leftCave = None
            if x > 0:
                upCave = self.caves[x-1][y]
            if y > 0:
                leftCave = newRow[-1]

            newRow.append(
                Cave(x, y, self.depth, self.target, upCave, leftCave))
        self.caves.append(newRow)

    def determineDanger(self):
        result = 0
        for x in range(self.target[1] + 1):
            for y in range(self.target[0] + 1):
                if not self.caves[x][y].geoSet:
                    self.caves[x][y].setGeoData()
                result += self.caves[x][y].type.value

        return result

    def followPath(self):
        gearSwapTime = 7

        visited = []
        caveQueue = []
        currentCave = self.caves[0][0]
        currentCave.distance = 0
        currentCave.gearOptions = [Gear.TORCH]
        caveQueue = []

        while currentCave != self.caves[self.target[1]][self.target[0]]:
            #self.activeCave = [currentCave.x, currentCave.y]
            # print(self)
            # input()
            for diffX in range(-1, 2):
                for diffY in range(-1, 2):
                    if diffX == 0 and diffY == 0 or diffX != 0 and diffY != 0:
                        continue

                    x = diffX + currentCave.x
                    y = diffY + currentCave.y
                    if x < 0 or y < 0 or x >= self.depth or y >= self.depth:
                        continue

                    if x >= len(self.caves):
                        self.addRow()
                    if y >= len(self.caves[0]):
                        self.addCol()

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

            visited.append(currentCave)
            currentCave = heapq.heappop(caveQueue)
            prevGearOptions = currentCave.cameFromCave.gearOptions

            # 0 match
            if not ALLOWED_GEAR[currentCave.type][0] in prevGearOptions and not ALLOWED_GEAR[currentCave.type][1] in prevGearOptions:
                currentCave.gearOptions = ALLOWED_GEAR[currentCave.type]

            # 2 match; going to same type
            elif ALLOWED_GEAR[currentCave.type][0] in prevGearOptions and ALLOWED_GEAR[currentCave.type][1] in prevGearOptions:
                currentCave.gearOptions = prevGearOptions

            # 1 match
            else:
                if prevGearOptions[0] in ALLOWED_GEAR[currentCave.type]:
                    nextGear = prevGearOptions[0]
                elif prevGearOptions[1] in ALLOWED_GEAR[currentCave.type]:
                    nextGear = prevGearOptions[1]
                currentCave.gearOptions = [nextGear]

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
    return CaveSystem(depth, target).determineDanger()


def part2(data):
    depth, target = parseInput(data)
    caveSystem = CaveSystem(depth, target)
    caveSystem.followPath()
    return caveSystem.caves[target[0]][target[1]].distance
