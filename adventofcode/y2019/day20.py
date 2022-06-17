import sys
import heapq
import numpy as np


class MazeTile:
    def __init__(self, x, y, floorType) -> None:
        self.x = x
        self.y = y
        self.neighbors = []
        self.floorType = floorType
        self.walkable = self.floorType == "."
        self.distance = sys.maxsize

    def __str__(self) -> str:
        if self.walkable:
            if self.distance < sys.maxsize:
                return "{:2d}".format(self.distance)
            else:
                return ". "
        else:
            return self.floorType + " "

    def __lt__(self, __o: object) -> bool:
        return self.distance < __o.distance

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, MazeTile):
            return False
        return self.x == __o.x and self.y == __o.y

    def addNeighbors(self, neighborCoords, maze):
        for coords in neighborCoords:
            x = coords[0]
            y = coords[1]
            self.neighbors.append(maze[x][y])


class TorusMaze:
    def __init__(self, mapString) -> None:
        self.rawMap = [x for x in [y for y in mapString]]
        self.maxWidth = 0
        self.start = None
        self.end = None
        for row in self.rawMap:
            self.maxWidth = max(self.maxWidth, len(row))

        self.map = []
        warpIDKey = {}
        warpTiles = []
        for x in range(len(self.rawMap)):
            mapRow = []
            for y in range(self.maxWidth):
                if y >= len(self.rawMap[x]):
                    mapRow.append(MazeTile(x, y, " "))
                elif self.rawMap[x][y] in [" ", "#", "."]:
                    mapRow.append(MazeTile(x, y, self.rawMap[x][y]))
                else:
                    neighbors = self.getNeighbors(x, y)
                    if len(neighbors) == 2:
                        if self.rawMap[neighbors[0][0]][neighbors[0][1]] == ".":
                            warpCoords = neighbors[0]
                            warpID = self.getWarpID([x, y], neighbors[1])
                        else:
                            warpCoords = neighbors[1]
                            warpID = self.getWarpID([x, y], neighbors[0])

                        if warpID == "AA":
                            self.start = warpCoords
                        elif warpID == "ZZ":
                            self.end = warpCoords
                        else:
                            if not warpID in warpIDKey:
                                warpIDKey[warpID] = []
                            warpTiles.append(
                                "{}_{}".format(warpCoords[0], warpCoords[1])
                            )
                            warpIDKey[warpID].append(warpCoords)
                    mapRow.append(MazeTile(x, y, " "))
            self.map.append(mapRow)

        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if self.map[x][y].walkable:
                    neighbors = self.getNeighbors(x, y, False)
                    self.map[x][y].addNeighbors(
                        self.getNeighbors(x, y, False), self.map
                    )

        for warpID in warpIDKey:
            if len(warpIDKey[warpID]) == 2:
                warp1 = warpIDKey[warpID][0]
                warp2 = warpIDKey[warpID][1]
                self.map[warp1[0]][warp1[1]].addNeighbors([warp2], self.map)
                self.map[warp2[0]][warp2[1]].addNeighbors([warp1], self.map)

    def __str__(self) -> str:
        result = ""
        for x in range(len(self.map)):
            row = ""
            for y in range(len(self.map[x])):
                if [x, y] == self.start:
                    row += "S"
                elif [x, y] == self.end:
                    row += "E"
                else:
                    row += str(self.map[x][y])
            result += "\n" + row
        return result

    def getNeighbors(self, _x, _y, useRaw=True):
        result = []
        for diffX in range(-1, 2):
            for diffY in range(-1, 2):
                if diffX == 0 and diffY == 0:
                    continue
                if diffX != 0 and diffY != 0:
                    continue

                x = diffX + _x
                y = diffY + _y

                if x < 0 or y < 0 or x >= len(self.rawMap) or y >= self.maxWidth:
                    continue
                if useRaw:
                    if y < len(self.rawMap[x]) and not self.rawMap[x][y] in [" ", "#"]:
                        result.append([x, y])
                else:
                    if self.map[x][y].walkable:
                        result.append([x, y])

        return result

    def getWarpID(self, point1, point2):
        if point1[0] == point2[0]:
            if point1[1] < point2[1]:
                return (
                    self.rawMap[point1[0]][point1[1]]
                    + self.rawMap[point2[0]][point2[1]]
                )
            else:
                return (
                    self.rawMap[point2[0]][point2[1]]
                    + self.rawMap[point1[0]][point1[1]]
                )
        else:
            if point1[0] < point2[0]:
                return (
                    self.rawMap[point1[0]][point1[1]]
                    + self.rawMap[point2[0]][point2[1]]
                )
            else:
                return (
                    self.rawMap[point2[0]][point2[1]]
                    + self.rawMap[point1[0]][point1[1]]
                )

    def findPath(self):
        self.map[self.start[0]][self.start[1]].distance = 0

        tileQueue = [self.map[self.start[0]][self.start[1]]]
        visited = []
        while len(tileQueue) != 0:
            currentTile = heapq.heappop(tileQueue)

            for neighbor in currentTile.neighbors:
                neighbor.distance = min(neighbor.distance, currentTile.distance + 1)
                if not neighbor in visited and not neighbor in tileQueue:
                    heapq.heappush(tileQueue, neighbor)
            visited.append(currentTile)

        return self.map[self.end[0]][self.end[1]].distance


def part1(data, test=False) -> str:
    torusMaze = TorusMaze(data)
    return torusMaze.findPath()


def part2(data, test=False) -> str:
    return "Wut?"
