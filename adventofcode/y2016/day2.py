
def getCode(keyPad, data, startPos=[1, 1]):
    position = startPos.copy()
    result = ""
    for line in data:
        for letter in line:
            nextPosition = position.copy()
            if letter == "U":
                nextPosition[0] -= 1
            elif letter == "L":
                nextPosition[1] -= 1
            elif letter == "R":
                nextPosition[1] += 1
            elif letter == "D":
                nextPosition[0] += 1

            if nextPosition[0] < 0:
                nextPosition[0] = 0
            if nextPosition[0] > len(keyPad) - 1:
                nextPosition[0] = len(keyPad) - 1

            if nextPosition[1] < 0:
                nextPosition[1] = 0
            if nextPosition[1] > len(keyPad) - 1:
                nextPosition[1] = len(keyPad) - 1

            if keyPad[nextPosition[0]][nextPosition[1]] == 0:
                continue
            position = nextPosition
        result += str(keyPad[position[0]][position[1]])
    return result


def part1(data):
    keyPad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return getCode(keyPad, data)


def part2(data):
    keyPad = [[0, 0, 1, 0, 0],
              [0, 2, 3, 4, 0],
              [5, 6, 7, 8, 9],
              [0, 'A', 'B', 'C', 0],
              [0, 0, 'D', 0, 0]]
    return getCode(keyPad, data, [3, 0])
