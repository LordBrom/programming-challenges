from aoc import manhattan_distance
import re

RE_STR = "Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)"

def part1(data, test=False) -> str:
	if test:
		y = 10
	else:
		y = 2000000

	beacons = set()
	scanned = set()

	for d in data:
		reResult = re.search(RE_STR, d)
		sensor = (int(reResult.group(1)), int(reResult.group(2)))
		beacon = (int(reResult.group(3)), int(reResult.group(4)))
		beacons.add(beacon)
		dist = manhattan_distance(sensor, beacon)
		for x in range(int(sensor[0] - dist), int(sensor[0] + dist + 1)):
			if manhattan_distance(sensor, (x, y)) <= dist:
				scanned.add((x,y))

	return str(len(scanned - beacons))


def part2(data, test=False) -> str:
	if test:
		maxPos = 20
	else:
		maxPos = 4000000

	sensors = []
	for d in data:
		reResult = re.search(RE_STR, d)
		sensor = (int(reResult.group(1)), int(reResult.group(2)))
		beacon = (int(reResult.group(3)), int(reResult.group(4)))

		sensors.append((sensor[0], sensor[1], int(manhattan_distance(sensor, beacon))))

	result = 0
	for sx, sy, dist in sensors:
		for p in range( dist + 1):
			for cx, cy in ( (sx - dist - 1 + p, sy - p),
							(sx + dist + 1 - p, sy - p),
							(sx - dist - 1 + p, sy + p),
							(sx + dist + 1 - p, sy + p) ):
				if 0 <= cx <= maxPos and 0 <= cy <= maxPos and \
					all(manhattan_distance((cx, cy), (ox, oy)) > od for ox, oy, od in sensors):
						result = cx * 4000000 + cy

	return str(result)
