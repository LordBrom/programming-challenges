def part1(data, test=False) -> str:
    data = data[0]
    floor = 0
    for d in data:
        if d == "(":
            floor += 1
        elif d == ")":
            floor -= 1
    return str(floor)


def part2(data, test=False) -> str:
    data = data[0]
    floor = 0
    result = None
    for i in range(len(data)):
        if data[i] == "(":
            floor += 1
        elif data[i] == ")":
            floor -= 1
        if floor == -1:
            result = i + 1
            break
    return str(result)
