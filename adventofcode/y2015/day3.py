def part1(data, test=False) -> str:
    santa = [0, 0]
    visited = set()
    visited.add("{}_{}".format(santa[0], santa[1]))

    for d in data:
        if d == "^":
            santa[1] += 1
        elif d == ">":
            santa[0] += 1
        elif d == "v":
            santa[1] -= 1
        elif d == "<":
            santa[0] -= 1

        visited.add("{}_{}".format(santa[0], santa[1]))

    return len(visited)


def part2(data, test=False) -> str:
    santa = [0, 0]
    roboSanta = [0, 0]
    visited = set()
    visited.add("{}_{}".format(santa[0], santa[1]))
    moveSanta = True

    for d in data:
        if d == "^":
            if moveSanta:
                santa[1] += 1
            else:
                roboSanta[1] += 1
        elif d == ">":
            if moveSanta:
                santa[0] += 1
            else:
                roboSanta[0] += 1
        elif d == "v":
            if moveSanta:
                santa[1] -= 1
            else:
                roboSanta[1] -= 1
        elif d == "<":
            if moveSanta:
                santa[0] -= 1
            else:
                roboSanta[0] -= 1

        if moveSanta:
            visited.add("{}_{}".format(santa[0], santa[1]))
        else:
            visited.add("{}_{}".format(roboSanta[0], roboSanta[1]))

        moveSanta = not moveSanta

    return len(visited)
