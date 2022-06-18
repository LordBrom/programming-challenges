import math
import re
from typing import List, Tuple
from aoc import manhattan_distance

RE_SCANNER_STR = "--- scanner ([0-9]+) ---"


def parseData(data):
    scannerNum = -1
    beacons = []
    scanners = {}
    readScanner = True
    for d in data:
        if d == "":
            if scannerNum != -1:
                scanners[scannerNum] = Scanner(scannerNum, beacons.copy())
            readScanner = True
            beacons = []
            continue
        elif readScanner:
            reScanner = re.search(RE_SCANNER_STR, d)
            scannerNum = int(reScanner.group(1))
            readScanner = False
            continue
        else:
            bSplit = d.split(",")
            newBeacons = [int(bSplit[0]), int(bSplit[1])]
            if len(bSplit) == 3:
                newBeacons.append(int(bSplit[2]))
            beacons.append(newBeacons)
    scanners[scannerNum] = Scanner(scannerNum, beacons.copy())
    return scanners


class Beacon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return str(self.x) + "," + str(self.y) + "," + str(self.z)

    def __eq__(self, other) -> bool:
        if "x" in other:
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return self.x == other[0] and self.y == other[1] and self.z == other[2]

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        if self.x != other.x:
            return self.x < other.x

        if self.y != other.y:
            return self.y < other.y

        return self.z < other.z

    def point(self, offset=[0, 0, 0], debug=False):
        if debug:
            print(self.x, offset[0])
            print(self.y, offset[0])
            print(self.z, offset[0])
        return [self.x + offset[0], self.y + offset[1], self.z + offset[2]]

    def diff(self, other):
        return [other.x - self.x, other.y - self.y, other.z - self.z]

    def rotatePoint(self, axis):
        point = [self.x, self.y, self.z]
        a = (0 + axis) % 3
        b = (1 + axis) % 3
        c = (2 + axis) % 3
        x = point[a]
        y = point[b]
        result = [0, 0, 0]
        result[a] = round(x * math.cos(math.pi / 2) + y * math.sin(math.pi / 2))
        result[b] = round(-x * math.sin(math.pi / 2) + y * math.cos(math.pi / 2))
        result[c] = point[c]
        return Beacon(result[a], result[b], result[c])

    def copy(self, offset=[0, 0, 0]):
        return Beacon(self.x + offset[0], self.y + offset[1], self.z + offset[2])


class Scanner:
    def __init__(self, num, beacons):
        self.num = num
        self.offset = None
        self.beacons = []

        for beacon in beacons:
            self.beacons.append(Beacon(beacon[0], beacon[1], beacon[2]))

        self.beaconRotations = {}
        self.setBeaconRotations()

    def setBeaconRotations(self):
        beacons = self.beacons.copy()
        for i in range(24):
            if i % 4 == 0 and i != 0:
                beacons = self.rotateBeacons(beacons)
                beacons = self.rotateBeacons(beacons, 1)
            if i % 12 == 0 and i != 0:
                beacons = self.rotateBeacons(beacons, 1)
                beacons = self.rotateBeacons(beacons, 2)
            if i % 20 == 0 and i != 0:
                beacons = self.rotateBeacons(beacons, 2)
                beacons = self.rotateBeacons(beacons, 2)
            self.beaconRotations[i] = beacons.copy()
            beacons = self.rotateBeacons(beacons)

    def printRange(self, scanRange=5):
        print("--- scanner", self.num, "---")
        for x in range(-scanRange, scanRange + 1):
            outStr = ""
            for y in range(-scanRange, scanRange + 1):
                if x == 0 and y == 0:
                    outStr += " S "
                elif [x, y] in self.beacons:
                    outStr += " B "
                else:
                    outStr += " . "
            print(outStr)

    def printPoints(self, includeRotations=False):
        if not includeRotations:
            print("--- scanner", self.num, "---")
            for b in self.beacons:
                print(b)
        else:
            for r in self.beaconRotations:
                # print("--- scanner", self.num, r, "---")
                for b in self.beaconRotations[r]:
                    print(b)

    def rotateBeacons(self, beacons, axis=0):
        result = []
        for beacon in beacons:
            result.append(beacon.rotatePoint(axis))
        return result

    def countOverlap(self, otherScanner):
        for rotation in otherScanner.beaconRotations:
            for otherBeacon in otherScanner.beaconRotations[rotation]:
                for beacon in self.beacons:
                    offset = otherBeacon.diff(beacon)
                    count = 0
                    checked = 0
                    minToCheck = (len(otherScanner.beaconRotations[rotation]) - 12) + 1
                    for check in otherScanner.beaconRotations[rotation]:
                        checked += 1
                        if check.point(offset) in self.beacons:
                            count += 1
                            if count >= 12:
                                self.addBeacons(
                                    otherScanner.beaconRotations[rotation], offset
                                )
                                return True, offset
                        if checked >= minToCheck + count:
                            break
        return False, None

    def addBeacons(self, beacons, offset=[0, 0, 0]):
        for p in beacons:
            newBeacon = p.copy(offset)
            if not newBeacon.point() in self.beacons:
                self.beacons.append(newBeacon)


def part1(data, test=False) -> str:
    scanners = parseData(data)
    scannersFound = [0]
    noneFound = True
    while len(scannersFound) < len(scanners):
        print("Starting new loop", end="", flush=True)
        for i in range(1, len(scanners)):
            if not i in scannersFound:
                print(". ", end="", flush=True)
                scannerOffset = scanners[0].countOverlap(scanners[i])
                if scannerOffset[0]:
                    print()
                    print("adding", i, "at", scannerOffset[1])
                    noneFound = False
                    scannersFound.append(i)
                    break
        if noneFound:
            print("none found")

    return str(len(scanners[0].beacons))


def part2(data, test=False) -> str:
    scanners = parseData(data)
    scannersFound = [0]
    scanners[0].offset = [0, 0, 0]
    while len(scannersFound) < len(scanners):
        for i in range(1, len(scanners)):
            if not i in scannersFound:
                scannerOffset = scanners[0].countOverlap(scanners[i])
                if scannerOffset[0]:
                    scanners[i].offset = scannerOffset[1]
                    scannersFound.append(i)
                    break

    result = 0

    for i in range(len(scanners)):
        for j in range(len(scanners)):
            if i == j:
                continue
            result = max(
                result, int(manhattan_distance(scanners[i].offset, scanners[j].offset))
            )

    return str(result)
