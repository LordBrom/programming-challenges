import heapq


def getNeighbors(x, y, grid):
    adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbors = []
    for dx, dy in adjacent:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            neighbors.append((nx, ny))
    return neighbors


def dijkstra(grid):
    start = (0, 0)
    end = (len(grid[0]) - 1, len(grid) - 1)
    dist_heap = [(0, start)]
    visited = set()

    while True:
        dist, current = heapq.heappop(dist_heap)
        if current in visited:
            continue
        visited.add(current)
        if current == end:
            return dist

        for n in getNeighbors(current[0], current[1], grid):
            x, y = n
            n_cost = grid[x][y] + dist
            heapq.heappush(dist_heap, (n_cost, n))


def part1(data, test=False) -> str:
    cave = []
    for d in data:
        cave.append([int(x) for x in d])
    return dijkstra(cave)


def part2(data, test=False) -> str:
    cave = []

    for yi in range(5):
        for dataRow in data:
            row = []
            for xi in range(5):
                for n in dataRow:
                    row.append((((int(n) + xi + yi) - 1) % 9) + 1)

            cave.append(row.copy())
    return dijkstra(cave)
