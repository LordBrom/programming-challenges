import re


RE_STR = "Valve ([A-Z]+) has flow rate=([0-9]+); tunnel(s|) lead(s|) to valve(s|) (.+)"


class Valve():
	def __init__(self, name, rate, leads) -> None:
		self.name = name
		self.rate = rate
		self.leads = leads

	def follow_path(self, valves, visited = [], time = 0, pressure = 0, released = set()):
		visited.append(self.name)

		best = pressure
		bestVisited = visited

		if time >= 30:
			return best, bestVisited

		for lead in self.leads:
			#skip = False
			#for i in [x for x,val in enumerate(visited) if val == self.name]:
			#	if i + 1 == len(visited):
			#		continue
			#	if visited[i + 1] == lead:
			#		skip = True

			#if skip:
			#	continue
			if (len(visited) >= 2 and lead == visited[-2]) and len(self.leads) != 1:
				continue

			if not self.name in released and self.rate != 0:
				newReleased = released.copy()
				newReleased.add(self.name)
				check, checkVisit = valves[lead].follow_path(valves, visited.copy(), time + 2, pressure + (self.rate * (29 - time)), newReleased)


				if check >= best:
					best = check
					bestVisited = checkVisit

			check, checkVisit = valves[lead].follow_path(valves, visited.copy(), time + 1, pressure, released)

			if check >= best:
				best = check
				bestVisited = checkVisit

		return best, bestVisited

	def elephant_path(self):
		pass


def part1(data, test=False) -> str:
	valves = {}
	for d in data:
		reResult = re.search(RE_STR, d)
		name = reResult.group(1)
		rate = int(reResult.group(2))
		leads = reResult.group(6)
		valves[name] = Valve(name, rate, leads.split(", "))
	return str(valves["AA"].follow_path(valves)[0])

def part2(data, test=False) -> str:
	return "not implemented"
