import re

RECOORD = "([0-9]+), ([0-9]+)"


class Grid:
    def __init__(self):
        width = 360
        self.grid = []
        self.points = []
        for x in range(width):
            self.grid.append([[0, -1] for x in range(width)])

    def add_point(self, y, x, part1=True):
        newLetter = 1 + len(self.points)
        self.grid[x][y] = [newLetter, 0]
        self.points.append([x, y])

        if part1:
            for i in range(len(self.grid)):
                for j in range(len(self.grid[x])):
                    dist = self.distance([x, y], [i, j])
                    if [i, j] in self.points:
                        continue
                    elif self.grid[i][j][1] == -1 or self.grid[i][j][1] > dist:
                        self.grid[i][j][0] = newLetter
                        self.grid[i][j][1] = dist
                    elif self.grid[i][j][1] == dist:
                        self.grid[i][j][0] = 0

    def print_grid(self):
        for x in self.grid:
            rowStr = ""
            for y in x:
                if (y[1] == -1):
                    rowStr += " ."
                else:
                    rowStr += " " + str(y[0]) + ""
            print(rowStr)

    def distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

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
                    if x == len(self.grid) - 1 or y == len(self.grid[x]) - 1 or y == 0 or x == 0:
                        infResults.append(point)

        for i in results:
            if i in infResults:
                results[i] = -1

        return results


def part1(input):
    grid = Grid()
    for i in input:
        reResult = re.search(RECOORD, i)
        grid.add_point(int(reResult.group(1)), int(reResult.group(2)))
    result = 0
    pointCounts = grid.count_points()
    for i in pointCounts:
        result = max(int(result), pointCounts[i])
    return result


def part2(input):
    return "not implemented"
