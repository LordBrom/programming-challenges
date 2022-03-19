
def part1(data):
    result = 0
    for i in range(len(data)):
        if data[i] == data[(i + 1) % len(data)]:
            result += int(data[i])
    return result


def part2(data):
    result = 0
    for i in range(len(data)):
        if data[i] == data[int(i + (len(data) / 2)) % len(data)]:
            result += int(data[i])
    return result
