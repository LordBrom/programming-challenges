from hashlib import md5


def getOpenDoors(passCode):
    md5Result = md5(passCode.encode()).hexdigest()
    result = []
    for i in range(4):
        if md5Result[i] in ["b", "c", "d", "e", "f"]:
            result.append(i)

    return result


def followPath(code, path="", position=[0, 0], shortest=True):
    if position == [3, 3]:
        return path

    best = None

    openDoors = getOpenDoors(code + path)
    for door in openDoors:
        newPosition = position.copy()
        newPath = path
        if door == 0:
            if position[0] == 0:
                continue
            newPosition[0] -= 1
            newPath += "U"
        elif door == 1:
            if position[0] == 3:
                continue
            newPosition[0] += 1
            newPath += "D"
        elif door == 2:
            if position[1] == 0:
                continue
            newPosition[1] -= 1
            newPath += "L"
        elif door == 3:
            if position[1] == 3:
                continue
            newPosition[1] += 1
            newPath += "R"

        check = followPath(code, newPath, newPosition, shortest)
        if shortest and (best == None or (check != None and len(check) < len(best))):
            best = check
        elif not shortest and (
            best == None or (check != None and len(check) > len(best))
        ):
            best = check

    return best


def part1(data, test=False) -> str:
    data = data[0]
    return followPath(data)


def part2(data, test=False) -> str:
    data = data[0]
    return str(len(followPath(data, shortest=False)))
