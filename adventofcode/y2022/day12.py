from collections import deque
from aoc import get_neighbors

def make_map(data):
	map = []
	start = None
	end = None
	starts = []
	for row in range(len(data)):
		mapRow = []
		for col in range(len(data[row])):
			if data[row][col] == 'S':
				start = (col, row)
				starts.append((col, row))
				mapRow.append(0)
			elif data[row][col] == 'E':
				end = (col, row)
				mapRow.append(25)
			elif data[row][col] == 'a':
				starts.append((col, row))
				mapRow.append(0)
			else:
				mapRow.append(ord(data[row][col]) - 97)
		map.append(mapRow)
	return map, start, end, starts

def get_dist(grid, start, end):
	visited = {}
	visited[start] = 0

	to_visit = deque()
	to_visit.append(start)

	while to_visit:
		(cx, cy) = to_visit.popleft()
		current_steps = visited[(cx, cy)]
		for n in get_neighbors(grid, cx, cy):
			nx, ny = n
			if (nx, ny) in visited:
				continue
			if grid[ny][nx] - grid[cy][cx] <= 1:
				visited[(nx, ny)] = current_steps + 1
				to_visit.append((nx, ny))

				if (nx, ny) == end:
					return current_steps+1

	return None

def part1(data, test=False) -> str:
	heightMap, start, end, starts = make_map(data)
	return str(get_dist(heightMap, start, end))


def part2(data, test=False) -> str:
	heightMap, start, end, starts = make_map(data)
	results = []
	for s in starts:
		test = get_dist(heightMap, s, end)
		if test != None:
			results.append(get_dist(heightMap, s, end))
	results.sort()
	return str(results[0])
