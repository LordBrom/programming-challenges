def part1(input):
    result = 0

    n = 0
    first = True

    for i in input:
        if not first:
            if int(i) > int(n):
                result += 1
        n = i
        first = False

    return result


def part2(input):
    windowSum = []
    for i in range(len(input) - 2):
        windowSum.append(int(input[i]) + int(input[i + 1]) + int(input[i + 2]))

    return part1(windowSum)
