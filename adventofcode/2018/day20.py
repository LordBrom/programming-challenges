import sys
from unittest import result


class Room():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.doors = {
            'N': None,
            'S': None,
            'E': None,
            'W': None
        }
        self.distFromStart = sys.maxsize

    def __str__(self) -> str:
        return "Room at {}, {}. Connects to N: {}, E: {}, S: {}, W: {}".format(
            self.x, self.y, self.doors['N'] != None, self.doors['E'] != None, self.doors['S'] != None, self.doors['W'] != None)

    def __eq__(self, __o: object) -> bool:
        if __o != None and __o.x != None and __o.y != None:
            return self.x == __o.x and self.y == __o.y
        else:
            return False

    def xy(self, asStr=False):
        if asStr:
            return "{}_{}".format(self.x, self.y)
        return [self.x, self.y]

    def addDoors(self, doors):
        if 'N' in doors:
            self.doors['N'] = doors['N']
        if 'S' in doors:
            self.doors['S'] = doors['S']
        if 'E' in doors:
            self.doors['E'] = doors['E']
        if 'W' in doors:
            self.doors['W'] = doors['W']

    def openDoors(self, visited=[]):
        result = []
        if not self.doors['N'] in visited and self.doors['N'] != None:
            result.append('N')
        if not self.doors['S'] in visited and self.doors['S'] != None:
            result.append('S')
        if not self.doors['E'] in visited and self.doors['E'] != None:
            result.append('E')
        if not self.doors['W'] in visited and self.doors['W'] != None:
            result.append('W')

        return result

    def setDistFromStart(self, val):
        self.distFromStart = min(self.distFromStart, val)


class ConstructionZone():
    def __init__(self) -> None:
        self.rooms = {}
        self.rooms["0_0"] = Room(0, 0)

    def followPath(self, path, startX=0, startY=0):
        room = self.rooms[str(startX) + "_" + str(startY)]
        i = 0
        while i < len(path):
            p = path[i]
            if p in ['N', 'S', 'E', 'W']:
                if p == 'N':
                    newX = room.x
                    newY = room.y + 1
                    fromDir = 'S'
                    toDir = 'N'
                elif p == 'S':
                    newX = room.x
                    newY = room.y - 1
                    fromDir = 'N'
                    toDir = 'S'
                elif p == 'E':
                    newX = room.x + 1
                    newY = room.y
                    fromDir = 'W'
                    toDir = 'E'
                elif p == 'W':
                    newX = room.x - 1
                    newY = room.y
                    fromDir = 'E'
                    toDir = 'W'

                if not str(newX) + "_" + str(newY) in self.rooms:
                    self.rooms[str(newX) + "_" + str(newY)] = Room(newX, newY)

                newRoom = self.rooms[str(newX) + "_" + str(newY)]
                room.addDoors({toDir: newRoom})
                newRoom.addDoors({fromDir: room})
                room = newRoom
            elif p == "(":
                subPath, i = self.getSubPath(path, i)
                splitPos = self.getSplitPos(subPath)
                start = 0
                for s in splitPos:
                    self.followPath(subPath[start:s], room.x, room.y)
                    start = s + 1
                self.followPath(subPath[start:], room.x, room.y)
            i += 1

    def getSubPath(self, path, startPos):
        i = startPos + 1
        openCount = 1
        while openCount > 1 or path[i] != ')':
            if path[i] == ")":
                openCount -= 1
            elif path[i] == "(":
                openCount += 1
            i += 1
        return path[startPos + 1: i], i

    def getSplitPos(self, path):
        openCount = 0
        result = []
        for i in range(len(path)):

            if path[i] == ")":
                openCount -= 1
            elif path[i] == "(":
                openCount += 1
            elif openCount == 0 and path[i] == '|':
                result.append(i)

        return result

    def followRoute(self, startPoint=[0, 0], path=[]):
        best = path
        x = startPoint[0]
        y = startPoint[1]
        currentRoom = self.rooms["{}_{}".format(x, y)]
        currentRoom.setDistFromStart(len(path))
        openDoors = currentRoom.openDoors(path)
        path.append(currentRoom)

        while len(openDoors) > 0:
            if len(openDoors) == 1:
                nextDir = openDoors[0]
                currentRoom = currentRoom.doors[nextDir]
                currentRoom.setDistFromStart(len(path))
                path.append(currentRoom)
                openDoors = currentRoom.openDoors(path)
            else:
                for dir in openDoors:
                    check = self.followRoute(
                        currentRoom.doors[dir].xy(), path.copy())

                    if len(check) > len(best):
                        best = check.copy()
                return best
        return best


def flipDir(dir):
    if dir == 'N':
        return 'S'

    if dir == 'S':
        return 'N'

    if dir == 'E':
        return 'W'

    if dir == 'W':
        return 'E'


def part1(data):
    pathReStr = data[1:-1]
    constructionZone = ConstructionZone()
    constructionZone.followPath(pathReStr)
    return len(constructionZone.followRoute()) - 1


def part2(data):
    pathReStr = data[1:-1]
    constructionZone = ConstructionZone()
    constructionZone.followPath(pathReStr)
    constructionZone.followRoute([0, 0], [])
    result = 0
    for r in constructionZone.rooms:
        if constructionZone.rooms[r].distFromStart >= 1000:
            result += 1
    return result
