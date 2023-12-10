import re

def parse_input(data):
    timeSplit = data[0].split(":")[1]
    distanceSplit = data[1].split(":")[1]
    reStr = "[0-9]+"

    times = [int(x) for x in re.findall(reStr, timeSplit)]
    distances = [int(x) for x in re.findall(reStr, distanceSplit)]

    return times, distances

def run_race(time, goal):
    won = False
    ways = 0
    for t in range(time + 1):
        time_left = time - t
        dist = time_left * t
        if dist > goal:
            won = True
            ways += 1

    return won, ways

def part1(data, test=False) -> str:
    times, distances = parse_input(data)
    result = 1

    for i in range(len(times)):
        won, ways = run_race(times[i], distances[i])
        if won:
            result *= ways

    return str(result)

def part2(data, test=False) -> str:
    data[0] = data[0].replace(" ", "")
    data[1] = data[1].replace(" ", "")
    times, distances = parse_input(data)

    _, ways = run_race(times[0], distances[0])

    return str(ways)
