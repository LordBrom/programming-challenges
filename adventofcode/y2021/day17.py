import re

RE_STR = "target area: x=([-0-9]+)..([-0-9]+), y=([-0-9]+)..([-0-9]+)"


def trackProbe(velocity, target):
    probePosition = [0, 0]
    maxY = 0

    while True:
        probePosition[0] += velocity[0]
        probePosition[1] += velocity[1]

        maxY = max(maxY, probePosition[1])

        if velocity[0] > 0:
            velocity[0] -= 1
        elif velocity[0] < 0:
            velocity[0] += 1

        velocity[1] -= 1

        inXRange = target[0][0] <= probePosition[0] <= target[0][1]
        inYRange = target[1][0] <= probePosition[1] <= target[1][1]

        if inXRange and inYRange:
            return (True, maxY)

        pastXRange = probePosition[0] > target[0][1]
        pastYRange = probePosition[1] <= target[1][0]

        if pastXRange or pastYRange:
            return (False, maxY)


def part1(data, test=False) -> str:
    reResult = re.search(RE_STR, data[0])
    xRange = (int(reResult.group(1)), int(reResult.group(2)))
    yRange = (int(reResult.group(3)), int(reResult.group(4)))

    result = 0

    for x in range(0, xRange[1] + 1):
        for y in range(yRange[0], -yRange[0]):
            success, maxY = trackProbe([x, y], [xRange, yRange])
            if success:
                result = max(result, maxY)
    return str(result)


def part2(data, test=False) -> str:
    reResult = re.search(RE_STR, data[0])
    xRange = (int(reResult.group(1)), int(reResult.group(2)))
    yRange = (int(reResult.group(3)), int(reResult.group(4)))

    results = 0

    for x in range(0, xRange[1] + 1):
        for y in range(yRange[0], -yRange[0]):
            if trackProbe([x, y], [xRange, yRange])[0]:
                results += 1
    return str(results)
