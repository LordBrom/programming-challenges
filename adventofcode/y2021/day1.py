def part1(data, test=False) -> str:
    result = 0

    n = 0
    first = True

    for i in data:
        if not first:
            if int(i) > int(n):
                result += 1
        n = i
        first = False

    return result


def part2(data):
    windowSum = []
    for i in range(len(data) - 2):
        windowSum.append(int(data[i]) + int(data[i + 1]) + int(data[i + 2]))

    return part1(windowSum)
