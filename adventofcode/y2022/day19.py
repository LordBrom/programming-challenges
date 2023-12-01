import re
import sys
from heapq import heappop
import collections

RE_STR = "Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian."

def optimistic_upper(resources, robots, time):
	result = ((time + robots[3]) * (time + robots[3] + 1)) // 2
	result -= (robots[3] * (robots[3] + 1)) // 2
	result += resources[3]
	return result

def should_wait(resources, robots, maxResources):
	for i in range(len(robots)):
		if robots[i] > 0 and resources[i] < maxResources[i]:
			return True
	return False

def run_blueprint(blueprint, time = 24):
	maxResources = [max([bp[i] for bp in blueprint]) for i in range(len(blueprint))]
	maxResources[3] = sys.maxsize

	queue = [(0, time, (0, 0, 0, 0), (1, 0, 0, 0))]

	result = 0
	stateCache = collections.defaultdict(lambda: -1)

	while queue:
		_, timeLeft, resources, robots = heappop(queue)
		result = max(result, resources[3] + robots[3]*timeLeft)

		if optimistic_upper(resources, robots, timeLeft) <= result:
			continue

		cacheKey = (timeLeft, resources[:3], robots)
		if stateCache[cacheKey] > resources[3]:
			continue
		else:
			stateCache[cacheKey] = resources[3]

		if timeLeft == 0:
			continue

		if should_wait(resources, robots, maxResources):
			newResources = tuple(resource + robot for resource, robot in zip(resources, robots))
			newRobots = robots[:]
			queue.append((-newRobots[3], timeLeft - 1, newResources, newRobots))

		for ir, cost in enumerate(reversed(blueprint)):
			i = len(blueprint) - ir - 1
			if maxResources[i] > robots[i] \
					and all(resource >= price for resource, price in zip(resources, cost)):
				newResources = tuple(resource + robot - price for resource, robot, price in zip(resources, robots, cost))
				newRobots = tuple(robot + 1 if rx == i else robot for rx, robot in enumerate(robots))
				queue.append((-newRobots[3], timeLeft - 1, newResources, newRobots))

	return result

def parse_blueprints(data):
	blueprints = {}
	for d in data:
		reResult = re.search(RE_STR, d)
		blueprints[int(reResult.group(1))] = [
			[int(reResult.group(2)),0,0,0],
			[int(reResult.group(3)),0,0,0],
			[int(reResult.group(4)),int(reResult.group(5)), 0,0],
			[int(reResult.group(6)),0,int(reResult.group(7)),0]
		]
	return blueprints


def part1(data, test=False) -> str:
	blueprints = parse_blueprints(data)
	result = 0

	for i in blueprints:
		result += run_blueprint(blueprints[i], 24) * i
	return str(result)


def part2(data, test=False) -> str:
	blueprints = parse_blueprints(data)
	result = 1

	for i in range(1, 4):
		result *= run_blueprint(blueprints[i], 32)
	return str(result)
