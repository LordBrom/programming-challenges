import heapq

def trace_lava(cubes):
	result = 0
	position = [0,0,0]
	visited = set()
	to_visit = [(0,0,0)]

	while to_visit:
		position = heapq.heappop(to_visit)
		visited.add(f"{position[0]}_{position[1]}_{position[2]}")

		next = (position[0] + 1, position[1], position[2])
		nextPos = f"{next[0]}_{next[1]}_{next[2]}"
		if nextPos in cubes:
			result += 1
		elif next[0] > 30:
			pass
		elif not nextPos in visited and not next in to_visit:
			heapq.heappush(to_visit, next)

		next = (position[0] - 1, position[1], position[2])
		nextPos = f"{next[0]}_{next[1]}_{next[2]}"
		if nextPos in cubes:
			result += 1
		elif next[0] < -3:
			pass
		elif not nextPos in visited and not next in to_visit:
			heapq.heappush(to_visit, next)

		next = (position[0], position[1] + 1, position[2])
		nextPos = f"{next[0]}_{next[1]}_{next[2]}"
		if nextPos in cubes:
			result += 1
		elif next[1] > 30:
			pass
		elif not nextPos in visited and not next in to_visit:
			heapq.heappush(to_visit, next)

		next = (position[0], position[1] - 1, position[2])
		nextPos = f"{next[0]}_{next[1]}_{next[2]}"
		if nextPos in cubes:
			result += 1
		elif next[1] < -3:
			pass
		elif not nextPos in visited and not next in to_visit:
			heapq.heappush(to_visit, next)

		next = (position[0], position[1], position[2] + 1)
		nextPos = f"{next[0]}_{next[1]}_{next[2]}"
		if nextPos in cubes:
			result += 1
		elif next[2] > 30:
			pass
		elif not nextPos in visited and not next in to_visit:
			heapq.heappush(to_visit, next)

		next = (position[0], position[1], position[2] - 1)
		nextPos = f"{next[0]}_{next[1]}_{next[2]}"
		if nextPos in cubes:
			result += 1
		elif next[2] < -3:
			pass
		elif not nextPos in visited and not next in to_visit:
			heapq.heappush(to_visit, next)

	return result


def part1(data, test=False) -> str:
	cubes = []
	cubesStr = set()
	for d in data:
		cube = [int(x) for x in d.split(",")]
		cubesStr.add(f"{cube[0]}_{cube[1]}_{cube[2]}")
		cubes.append(cube)

	result = 0
	for cube in cubes:

		checkCube = f"{cube[0] + 1}_{cube[1]}_{cube[2]}"
		if not checkCube in cubesStr:
			result += 1
		checkCube = f"{cube[0] - 1}_{cube[1]}_{cube[2]}"
		if not checkCube in cubesStr:
			result += 1

		checkCube = f"{cube[0]}_{cube[1] + 1}_{cube[2]}"
		if not checkCube in cubesStr:
			result += 1
		checkCube = f"{cube[0]}_{cube[1] - 1}_{cube[2]}"
		if not checkCube in cubesStr:
			result += 1

		checkCube = f"{cube[0]}_{cube[1]}_{cube[2] + 1}"
		if not checkCube in cubesStr:
			result += 1
		checkCube = f"{cube[0]}_{cube[1]}_{cube[2] - 1}"
		if not checkCube in cubesStr:
			result += 1

	return str(result)


def part2(data, test=False) -> str:
	cubes = []
	cubesStr = set()

	for d in data:
		cube = [int(x) for x in d.split(",")]
		cubesStr.add(f"{cube[0]}_{cube[1]}_{cube[2]}")
		cubes.append(cube)

	return str(trace_lava(cubesStr))
