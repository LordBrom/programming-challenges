import sys


class PassageMap():
    def __init__(self, data) -> None:
        self.map = []
        self.start = []
        self.doors = {}
        self.keys = {}
        for x in range(len(data)):
            row = []
            for y in range(len(data[x])):
                letter = data[x][y]
                if letter.isalpha() and letter.lower() == letter:
                    self.keys[letter] = [x, y]
                elif letter.isalpha() and letter.upper() == letter:
                    self.doors[letter] = [x, y]

                if letter == "@":
                    self.start = [x, y]
                row.append(letter)
            self.map.append(row)

    def __str__(self) -> str:
        return self.printMap()

    def printMap(self, position=None) -> str:
        result = "--------------"

        for x in range(len(self.map)):
            rowStr = "\n"
            for y in range(len(self.map[x])):
                if [x, y] == position:
                    rowStr += "%"
                else:
                    rowStr += self.map[x][y]
            result += rowStr
        result += "\n--------------"
        return result

    def getAdjacent(self, pos, visited):
        result = []
        for difX in range(-1, 2):
            for difY in range(-1, 2):
                if difX == 0 and difY == 0:
                    continue
                if difX != 0 and difY != 0:
                    continue
                x = pos[0] - difX
                y = pos[1] - difY
                if x < 0 or x >= len(self.map):
                    continue
                if y < 0 or y >= len(self.map[x]):
                    continue
                if self.map[x][y].isalpha() and self.map[x][y].upper() == self.map[x][y]:
                    continue
                if self.map[x][y] != '#' and not [x, y] in visited:
                    result.append([x, y])
        return result

    def findChar(self, charToFind, position=None, path=[], depth=1):
        if position == None:
            position = self.start
        path.append(position)
        if self.map[position[0]][position[1]] == charToFind:
            return path, position
        movements = self.getAdjacent(position, path.copy())
        best = None
        lastPosition = None
        for m in movements:
            newPath, newPos = self.findChar(
                charToFind, m, path.copy(), depth + 1)
            if best == None or (newPath != None and len(best) > len(newPath)):
                best = newPath
                lastPosition = newPos
        return best, lastPosition

    def closestKey(self, pos, ignore=[]):
        best = (None, None)
        key = None
        for i in self.keys:
            if i in ignore:
                continue
            check = self.findChar(i, pos, [])
            if check[0] != None and (best[0] == None or len(check[0]) < len(best[0])):
                best = check
                key = i
        return (best[0], best[1], key)

    def unlockDoor(self, door):
        upDoor = door.upper()
        if upDoor in self.doors:
            doorPos = self.doors[upDoor]
            self.map[doorPos[0]][doorPos[1]] = "."

    def resetDoors(self):
        for door in self.doors:
            doorPos = self.doors[door]
            self.map[doorPos[0]][doorPos[1]] = door


def part1(data):
    passageMap = PassageMap(data)

    passageMap.resetDoors()
    path = []
    keyOrder = []
    curPos = passageMap.start

    unlockedDoors = []
    while len(unlockedDoors) < len(passageMap.keys):
        newPath, curPos, closestKey = passageMap.closestKey(
            curPos, unlockedDoors)
        newPath = newPath[1:]
        path.extend(newPath)
        passageMap.unlockDoor(closestKey)
        unlockedDoors.append(closestKey)
        keyOrder.append(closestKey)

    print(keyOrder)
    return len(path)


def part2(data):
    return "not implemented"
