import numpy as np

# 0: ^ up
# 1: > right
# 2: v down
# 3: < left


def dirHelp(inChar, ret=0):
    if inChar == "^" or inChar == 0:
        if ret == 0:
            return 0
        elif ret == 1:
            return "up"
        else:
            return "^"
    elif inChar == ">" or inChar == 1:
        if ret == 0:
            return 1
        elif ret == 1:
            return "right"
        else:
            return ">"
    elif inChar == "v" or inChar == 2:
        if ret == 0:
            return 2
        elif ret == 1:
            return "down"
        else:
            return "v"
    else:
        if ret == 0:
            return 3
        elif ret == 1:
            return "left"
        else:
            return "<"


class Track:
    def __init__(self, paths, carts) -> None:
        self.paths = paths
        self.carts = carts

    def __str__(self) -> str:
        cartPos = {}
        for c in self.carts:
            cartPos[c.posStr()] = dirHelp(c.direction, 2)
        result = ""
        for x in range(len(self.paths)):
            rowStr = ""
            for y in range(len(self.paths[x])):
                if "{}_{}".format(x, y) in cartPos:
                    rowStr += cartPos["{}_{}".format(x, y)]
                else:
                    rowStr += self.paths[x][y]
            result += "\n" + rowStr
        return result

    def moveCarts(self, returnFirst=True):
        cartPos = {}
        for c in self.carts:
            c.moved = False
            cartPos[c.posStr()] = c
        for x in range(len(self.paths)):
            for y in range(len(self.paths[x])):
                curCartPos = "{}_{}".format(x, y)
                if curCartPos in cartPos:
                    if cartPos[curCartPos].moved:
                        continue
                    cartPos[curCartPos].moved = True
                    nextX = x
                    nextY = y
                    if cartPos[curCartPos].direction == 0:
                        nextX -= 1
                    elif cartPos[curCartPos].direction == 1:
                        nextY += 1
                    elif cartPos[curCartPos].direction == 2:
                        nextX += 1
                    elif cartPos[curCartPos].direction == 3:
                        nextY -= 1

                    curCartNextPos = "{}_{}".format(nextX, nextY)
                    if curCartNextPos in cartPos:
                        self.carts.remove(cartPos[curCartPos])
                        self.carts.remove(cartPos[curCartNextPos])
                        if returnFirst:
                            return [nextX, nextY]
                    else:
                        cartPos[curCartPos].x = nextX
                        cartPos[curCartPos].y = nextY

                    cartPos[curCartPos].setNewDirection(self.paths[nextX][nextY])

                    cartPos[curCartNextPos] = cartPos[curCartPos]
                    del cartPos[curCartPos]
        return None


class Cart:
    def __init__(self, x, y, dirChar) -> None:
        self.x = x
        self.y = y
        self.direction = dirHelp(dirChar)
        self.turns = 0
        self.moved = False

    def __str__(self) -> str:
        return "facing {} at {}, {}".format(dirHelp(self.direction, 1), self.x, self.y)

    def posStr(self):
        return "{}_{}".format(self.x, self.y)

    def setNewDirection(self, tile):
        if tile == "+":
            turnDir = self.turns % 3
            if turnDir == 0:
                self.direction -= 1
            if turnDir == 2:
                self.direction += 1
            self.turns += 1
        elif tile == "\\":
            if self.direction == 0 or self.direction == 2:
                self.direction -= 1
            else:
                self.direction += 1
        elif tile == "/":
            if self.direction == 0 or self.direction == 2:
                self.direction += 1
            else:
                self.direction -= 1

        if self.direction < 0:
            self.direction = 3
        self.direction %= 4


def parseInput(data):
    maxLen = 0
    for i in range(len(data)):
        maxLen = max(maxLen, len(data[i]))

    track = []
    carts = []
    for x in range(len(data)):
        trackRow = []
        for y in range(maxLen):
            if y < len(data[x]):
                if data[x][y] in ["^", ">", "v", "<"]:
                    carts.append(Cart(x, y, data[x][y]))
                    if data[x][y] in [">", "<"]:
                        trackRow.append("-")
                    else:
                        trackRow.append("|")
                    pass
                else:
                    trackRow.append(data[x][y])
            else:
                trackRow.append(" ")
        track.append(trackRow)
    return Track(track, carts)


def part1(data, test=False) -> str:
    track = parseInput(data)
    firstCrash = None
    while firstCrash == None:
        firstCrash = track.moveCarts()
    return "{},{}".format(firstCrash[1], firstCrash[0])


def part2(data, test=False) -> str:
    track = parseInput(data)
    while len(track.carts) > 1:
        track.moveCarts(False)
    return "{},{}".format(track.carts[0].y, track.carts[0].x)
