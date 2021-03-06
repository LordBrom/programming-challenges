import re

RECOORD = "([0-9]+), ([0-9]+)"


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class Grid:
    def __init__(self, points):
        width = 360
        self.grid = []
        for i in range(width):
            self.grid.append([[-1, -1] for x in range(width)])

        self.points = points
        for p in range(len(self.points)):
            self.grid[self.points[p][0]][self.points[p][1]] = [p, 0]

    def print_grid(self, part1=True):
        nearPoints = self.count_near_points()
        for x in range(len(self.grid)):
            rowStr = ""
            for y in range(len(self.grid[x])):
                if part1:
                    if self.grid[x][y][1] == -1:
                        rowStr += " ."
                    else:
                        rowStr += " " + str(self.grid[x][y][0]) + ""
                else:
                    if not [x, y] in nearPoints:
                        rowStr += " ."
                    else:
                        rowStr += " #"

            print(rowStr)

    def fill_areas(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):

                for p in range(len(self.points)):
                    dist = distance(self.points[p], [i, j])
                    if [i, j] in self.points:
                        continue
                    elif self.grid[i][j][1] == -1 or self.grid[i][j][1] > dist:
                        self.grid[i][j][0] = p
                        self.grid[i][j][1] = dist
                    elif self.grid[i][j][1] == dist:
                        self.grid[i][j][0] = "x"

    def count_points(self):
        results = {}
        infResults = []
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                point = self.grid[x][y][0]
                if not point in results:
                    results[point] = 0
                results[point] += 1

                if not point in infResults:
                    if (
                        x == len(self.grid) - 1
                        or y == len(self.grid[x]) - 1
                        or y == 0
                        or x == 0
                    ):
                        infResults.append(point)

        for i in infResults:
            results.pop(i, None)

        return results

    def count_near_points(self, threshold=10000):
        results = []
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                pointDistTotal = 0
                for p in self.points:
                    pointDistTotal += distance(p, [x, y])
                if pointDistTotal < threshold:
                    results.append([x, y])
        return results


def parseInput(input):
    result = []
    for i in input:
        reResult = re.search(RECOORD, i)
        result.append([int(reResult.group(2)), int(reResult.group(1))])
    return result


def part1(data, test=False) -> str:
    grid = Grid(parseInput(data))
    grid.fill_areas()

    result = 0
    pointCounts = grid.count_points()
    for i in pointCounts:
        result = max(int(result), pointCounts[i])
    return str(result)


def part2(data, test=False) -> str:
    grid = Grid(parseInput(data))
    return str(len(grid.count_near_points()))
