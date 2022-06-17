def part1(input):

    result = 0

    for i in input:
        result += int(i)

    return result


def part2(input):

    result = 0
    found = {}
    i = 0

    while True:
        result += int(input[i % len(input)])
        i += 1
        try:
            if found[result]:
                return result
        except:
            found[result] = True
