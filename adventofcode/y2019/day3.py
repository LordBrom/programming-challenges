

def path_wire(path):
    posX = 0
    posY = 0
    result = []
    for i in path:
        wireDir = i[:1]
        wireLen = i[1:]
        for i in range(int(wireLen)):
            if wireDir == 'R':
                posX += 1
            elif wireDir == 'L':
                posX -= 1
            elif wireDir == 'U':
                posY += 1
            elif wireDir == 'D':
                posY -= 1

            result.append([posX, posY])
    return result


def path_wires(wire1, wire2):
    wire1Path = []
    wire2Path = []
    posX = 0
    posY = 0
    for i in wire1:
        wireDir = i[:1]
        wireLen = i[1:]
        for i in range(int(wireLen)):
            if wireDir == 'R':
                posX += 1
            elif wireDir == 'L':
                posX -= 1
            elif wireDir == 'U':
                posY += 1
            elif wireDir == 'D':
                posY -= 1

            wire1Path.append([posX, posY])

    minDist = 0

    posX = 0
    posY = 0
    for i in wire2:
        wireDir = i[:1]
        wireLen = i[1:]
        for i in range(int(wireLen)):
            if wireDir == 'R':
                posX += 1
            elif wireDir == 'L':
                posX -= 1
            elif wireDir == 'U':
                posY += 1
            elif wireDir == 'D':
                posY -= 1

            wire2Path.append([posX, posY])
            if [posX, posY] in wire1Path:
                calcDist = (len(wire2Path)) + (wire1Path.index([posX, posY]))
                if minDist == 0:
                    minDist = calcDist
                else:
                    minDist = min(calcDist, minDist)
    return minDist + 1


def part1(data):
    wire1 = data[0].split(',')
    wire2 = data[1].split(',')

    wirePath1 = path_wire(wire1)
    wirePath2 = path_wire(wire2)

    minDist = 0

    for i in wirePath1:
        if i[0] == 0 and i[1] == 0:
            continue
        elif i in wirePath2:
            calcDist = abs(0 - i[0]) + abs(0 - i[1])
            if minDist == 0:
                minDist = calcDist
            else:
                minDist = min(calcDist, minDist)

    return minDist


def part2(data):
    wire1 = data[0].split(',')
    wire2 = data[1].split(',')
    return path_wires(wire1, wire2)
