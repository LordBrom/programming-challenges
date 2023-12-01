import re
from collections import deque

RE_STR = "Valve ([A-Z]+) has flow rate=([0-9]+); tunnel(s|) lead(s|) to valve(s|) (.+)"

class Valve():
	def __init__(self, name, rate, leads) -> None:
		self.name = name
		self.rate = rate
		self.leads = leads
		self.dist = {}

def get_distances(valves, start, targets):
	dist = {start: 0}
	visited = {start}
	que = deque([start])
	while que and any(t not in dist for t in targets):
		current = que.popleft()
		for x in valves[current].leads:
			if x not in visited:
				visited.add(x)
				dist[x] = dist[current] + 1
				que.append(x)
	return dist


def find_paths(valves, time):
	pressures = []
	paths = []
	stack = [(time, 0, ['AA'])]

	while stack:
		time, pressure, path = stack.pop()
		current = path[-1]
		new = []
		for n, d in valves[current].dist.items():
			if d > time - 2 or n in path:
				continue
			tt = time - d - 1
			pp = pressure + valves[n].rate * tt
			s = tt, pp, path + [n]
			new.append(s)
		if new:
			stack.extend(new)
		else:
			pressures.append(pressure)
			paths.append(path[1:])

	return pressures, paths


def parse_input(data):
	valves = {}

	for d in data:
		reResult = re.search(RE_STR, d)
		name = reResult.group(1)
		rate = int(reResult.group(2))
		leads = reResult.group(6).split(", ")

		valves[name] = Valve(name, rate, leads)

	dist = {}
	nonZeroValves = [v for v in valves if valves[v].rate > 0]
	for start in ("AA", *nonZeroValves):
		dist[start] = {}
		d = get_distances(valves, start, nonZeroValves)
		for v in nonZeroValves:
			if v != start and v in d:
				dist[start][v] = d[v]
		valves[start].dist = dist[start].copy()

	return valves


def part1(data, test=False) -> str:
	valves = parse_input(data)
	return str(max(find_paths(valves, 30)[0]))

def part2(data, test=False) -> str:
	valves = parse_input(data)

	allPaths = list(zip(*find_paths(valves, 26)))
	p, paths = zip(*sorted(allPaths, reverse=True))

	i, j = 0, 1
	while any(x in paths[j] for x in paths[i]):
		j += 1

	result = p[i] + p[j]
	maxJ = j
	for i in range(1, maxJ):
		for j in range(i + 1, maxJ + 1):
			if any(x in paths[j] for x in paths[i]):
				continue
			result = max(result, p[i] + p[j])

	return str(result)
