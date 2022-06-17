import sys


class Key():
    def __init__(self, name, x, y) -> None:
        self.name = name
        self.x = x
        self.y = y
        self.distToKeys = {}

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Key):
            return False
        return self.name == __o.name

    def getPosition(self):
        return [self.x, self.y]


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
                    #self.keys[letter] = [x, y]
                    self.keys[letter] = Key(letter, x, y)
                elif letter.isalpha() and letter.upper() == letter:
                    self.doors[letter] = [x, y]

                if letter == "@":
                    self.start = [x, y]
                row.append(letter)
            self.map.append(row)

        for key in self.keys:
            for other in self.keys:
                if key == other:
                    continue
                test = self.findChar(
                    other, self.keys[key].getPosition(), list(self.keys.keys()), [])
                #print("here", test)
                if test[0] != None:
                    self.keys[key].distToKeys[other] = test[0]
            print(key, self.keys[key].distToKeys)

    def __str__(self) -> str:
        return self.printMap()

    def printMap(self, position=None, keysFound=[]) -> str:
        result = "--------------"

        for x in range(len(self.map)):
            rowStr = "\n"
            for y in range(len(self.map[x])):
                if [x, y] == position:
                    rowStr += "%"
                elif self.map[x][y].isalpha() and self.map[x][y].lower() in keysFound:
                    rowStr += "."
                else:
                    rowStr += self.map[x][y]
            result += rowStr
        result += "\n--------------"
        return result

    def getAdjacent(self, pos, visited, keysFound, sortTowards=None):
        result = []
        for difX in range(-1, 2):
            for difY in range(-1, 2):
                if difX == 0 and difY == 0:
                    continue
                if difX != 0 and difY != 0:
                    continue
                x = pos[0] + difX
                y = pos[1] + difY
                if x < 0 or x >= len(self.map):
                    result.append(None)
                    continue
                if y < 0 or y >= len(self.map[x]):
                    result.append(None)
                    continue
                if self.map[x][y].isalpha() and self.map[x][y].upper() == self.map[x][y]:
                    if not self.map[x][y].lower() in keysFound:
                        result.append(None)
                        continue
                if self.map[x][y] != '#' and not [x, y] in visited:
                    result.append([x, y])
                else:
                    result.append(None)
        if sortTowards:
            #print(pos, sortTowards, result)
            sortedResult = []
            if pos[0] < sortTowards.x:
                # x above
                if pos[1] < sortTowards.y:
                    # y above
                    sortedResult = [result[2], result[3], result[1], result[0]]
                elif pos[1] > sortTowards.y:
                    # y below
                    sortedResult = [result[1], result[3], result[2], result[0]]
                else:
                    # y same
                    sortedResult = [result[3], result[2], result[1], result[0]]
                pass
            elif pos[0] > sortTowards.x:
                # below
                if pos[1] < sortTowards.y:
                    # y above
                    sortedResult = [result[2], result[0], result[1], result[3]]
                elif pos[1] > sortTowards.y:
                    # y below
                    sortedResult = [result[1], result[0], result[2], result[3]]
                else:
                    # y same
                    sortedResult = [result[0], result[2], result[1], result[3]]
                pass
            else:
                # same
                if pos[1] < sortTowards.y:
                    # y above
                    sortedResult = [result[2], result[0], result[3], result[1]]
                elif pos[1] > sortTowards.y:
                    # y below
                    sortedResult = [result[1], result[0], result[3], result[2]]
                else:
                    # y same
                    # Should't ever be this
                    sortedResult = result
                pass
            result = sortedResult
            # print(result)
            # input()
        return result

    def findChar(self, charToFind, position=None, keysFound=[], path=[], best=None):
        if position == None:
            position = self.start
        path.append(position)
        if self.map[position[0]][position[1]] == charToFind:
            return path, position
        if best != None and len(best) <= len(path):
            return None, None
        movements = self.getAdjacent(
            position, path.copy(), keysFound, self.keys[charToFind])
        # best = None
        lastPosition = None
        for m in movements:
            if m == None:
                continue
            newPath, newPos = self.findChar(
                charToFind, m, keysFound, path.copy(), best)
            if best == None or (newPath != None and len(best) > len(newPath)):
                best = newPath
                lastPosition = newPos
        return best, lastPosition

    def availableKeys(self, pos, ignore=[]):
        result = []
        for key in self.keys:
            if key in ignore:
                continue
            found = self.findChar(key, pos, ignore, [])
            if found[0] != None:
                result.append([key, found])
        return result

    def findPath(self, position, path, keysFound, best=None):
        keyOptions = self.availableKeys(position, keysFound)
        bestRoute = None
        bestPath = None

        if len(keysFound) == len(self.keys):
            return len(path), keysFound, path
        if best != None and best <= len(path):
            return None, None, None

        print(keyOptions)

        keyOptions.sort(key=lambda x: len(x[1][0]))
        print(keyOptions)

        for option in keyOptions:
            tempPos = option[1][1]
            tempPath = path.copy()
            tempPath.extend(option[1][0][:-1])
            tempKeys = keysFound.copy()
            tempKeys.append(option[0])
            check, checkRoute, checkPath = self.findPath(
                tempPos, tempPath, tempKeys, best)
            if check != None and (best == None or check < best):
                best = check
                bestRoute = checkRoute
                bestPath = checkPath
        return best, bestRoute, bestPath


def part1(data):
    passageMap = PassageMap(data)
    print(passageMap)
    return
    #result = passageMap.findPath(passageMap.start, [], [])
    # return result[0]


def part2(data):
    return "not implemented"
