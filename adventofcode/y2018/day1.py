def part1(data, test=False) -> str:

    result = 0

    for i in data:
        result += int(i)

    return str(result)


def part2(data, test=False) -> str:

    result = 0
    found = {}
    i = 0

    while True:
        result += int(data[i % len(data)])
        i += 1
        try:
            if found[result]:
                return str(result)
        except:
            found[result] = True
