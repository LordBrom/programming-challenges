import sys


class HexTile:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return "{}, {}, {}".format(self.x, self.y, self.z)

    def get_dist(self):
        return max(abs(self.x), abs(self.y), abs(self.z))


class HexGrid:
    def __init__(self) -> None:
        self.tiles = {}
        centerTile = HexTile(0, 0, 0)
        # centerTile.dist = 0
        self.tiles["0_0_0"] = centerTile

    def follow_path(self, path):
        current = self.tiles["0_0_0"]
        furthest = 0

        for step in path:
            furthest = max(furthest, current.get_dist())

            if step == "n":
                nextCoords = [current.x, current.y - 1, current.z + 1]
            elif step == "ne":
                nextCoords = [current.x + 1, current.y - 1, current.z]
            elif step == "se":
                nextCoords = [current.x + 1, current.y, current.z - 1]
            elif step == "s":
                nextCoords = [current.x, current.y + 1, current.z - 1]
            elif step == "sw":
                nextCoords = [current.x - 1, current.y + 1, current.z]
            elif step == "nw":
                nextCoords = [current.x - 1, current.y, current.z + 1]
            nextCoordsStr = "{}_{}_{}".format(
                nextCoords[0], nextCoords[1], nextCoords[2]
            )

            if not nextCoordsStr in self.tiles:
                newTile = HexTile(nextCoords[0], nextCoords[1], nextCoords[2])
                newTile.dist = current.dist + 1
                self.tiles[nextCoordsStr] = newTile
                current = newTile
            else:
                current = self.tiles[nextCoordsStr]
        return current.get_dist(), furthest


def part1(data, test=False) -> str:
    data = data[0]
    hexGrid = HexGrid()
    return hexGrid.follow_path(data.split(","))[0]


def part2(data, test=False) -> str:
    data = data[0]
    hexGrid = HexGrid()
    return hexGrid.follow_path(data.split(","))[1]
