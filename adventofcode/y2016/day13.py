import sys
import heapq


class Tile():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.distFromStart = sys.maxsize
        self.isWall = None

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Tile) and self.x == __o.x and self.y == __o.y

    def __lt__(self, __o: object) -> bool:
        return self.distFromStart < __o.distFromStart

    def __str__(self) -> str:
        if self.isWall:
            return "#"
        else:
            return "."

    def setIsWall(self, num):
        xx = self.x * self.x
        x3 = 3 * self.x
        xy2 = 2 * self.x * self.y
        yy = self.y * self.y

        total = xx + x3 + xy2 + self.y + yy
        total += num

        oneCount = 0
        biStr = str(bin(total))
        for l in biStr:
            if l == "1":
                oneCount += 1

        self.isWall = oneCount % 2 == 1

    def getNeighbors(self, grid):
        adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        neighbors = []
        for dx, dy in adjacent:
            nx, ny = self.x+dx, self.y+dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[nx]) and not grid[nx][ny].isWall:
                neighbors.append((nx, ny))
        return neighbors


class OfficeSpace():
    def __init__(self, num, target=[31, 39]) -> None:
        self.num = num
        self.target = target

        self.space = []

        for x in range(target[0] + 500):
            rowSpace = []
            for y in range(target[1] + 500):
                newTile = Tile(x, y)
                newTile.setIsWall(num)
                rowSpace.append(newTile)
            self.space.append(rowSpace)

    def __str__(self) -> str:
        result = ""
        topStr = "   "
        for x in range(len(self.space)):
            if x <= 9:
                topStr += " "
            topStr += str(x) + " "
        result += topStr
        for x in range(len(self.space[0])):
            rowStr = str(x) + " "
            if x <= 9:
                rowStr += " "

            for y in range(len(self.space)):
                rowStr += " " + str(self.space[y][x]) + " "
            result += "\n" + rowStr
        return result

    def dijkstra(self):
        start = (1, 1)
        end = (self.target[0], self.target[1])
        dist_heap = [(0, start)]
        visited = set()

        while True:
            dist, current = heapq.heappop(dist_heap)
            if current in visited:
                continue
            visited.add(current)

            if current == end:
                return dist

            for n in self.space[current[0]][current[1]].getNeighbors(self.space):
                n_cost = 1 + dist
                heapq.heappush(dist_heap, (n_cost, n))

    def dijkstraMaxLength(self, maxLength=50):
        start = (1, 1)
        dist_heap = [(0, start)]
        visited = set()
        results = 0

        while True:
            dist, current = heapq.heappop(dist_heap)
            if current in visited:
                continue
            visited.add(current)

            if dist <= maxLength:
                results += 1

            if dist > maxLength:
                return results

            for n in self.space[current[0]][current[1]].getNeighbors(self.space):
                n_cost = 1 + dist
                heapq.heappush(dist_heap, (n_cost, n))


def part1(data):
    office = OfficeSpace(int(data))
    return office.dijkstra()


def part2(data):
    office = OfficeSpace(int(data))
    return office.dijkstraMaxLength()
