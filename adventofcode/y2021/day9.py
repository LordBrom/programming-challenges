def findLowPoints(heatMap):
    lowPoints = []

    for x in range(len(heatMap)):
        for y in range(len(heatMap[x])):
            num = heatMap[x][y]
            if x > 0 and heatMap[x - 1][y] <= num:
                continue
            if x < len(heatMap) - 1 and heatMap[x + 1][y] <= num:
                continue
            if y > 0 and heatMap[x][y - 1] <= num:
                continue
            if y < len(heatMap[x]) - 1 and heatMap[x][y + 1] <= num:
                continue
            lowPoints.append([x, y])
    return lowPoints


def findBasinSize(heatMap, startPoint, checked=[]):
    result = 1
    x = startPoint[0]
    y = startPoint[1]
    if heatMap[x][y] == 9:
        return 0

    if x > 0 and not [x - 1, y] in checked:
        checked.append([x - 1, y])
        result += findBasinSize(heatMap, [x - 1, y], checked)

    if x < len(heatMap) - 1 and not [x + 1, y] in checked:
        checked.append([x + 1, y])
        result += findBasinSize(heatMap, [x + 1, y], checked)

    if y > 0 and not [x, y - 1] in checked:
        checked.append([x, y - 1])
        result += findBasinSize(heatMap, [x, y - 1], checked)

    if y < len(heatMap[x]) - 1 and not [x, y + 1] in checked:
        checked.append([x, y + 1])
        result += findBasinSize(heatMap, [x, y + 1], checked)

    return result


def part1(data, test=False) -> str:
    heatMap = []
    for i in data:
        heatMap.append([int(char) for char in i])
    lowPoints = findLowPoints(heatMap)

    result = 0
    for p in lowPoints:
        result += int(heatMap[p[0]][p[1]]) + 1

    return result


def part2(data):
    heatMap = []
    for i in data:
        heatMap.append([int(char) for char in i])
    lowPoints = findLowPoints(heatMap)

    basins = []
    for p in lowPoints:
        basins.append(findBasinSize(heatMap, p) - 1)
    basins.sort()
    basins = basins[::-1]

    result = 1
    for i in range(3):
        result *= basins[i]

    return result
