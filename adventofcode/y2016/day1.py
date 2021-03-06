import re
from aoc import manhattan_distance

def followPath(path, stopAtHQ=False, start=[0, 0]):
    reResult = re.findall("(R|L)([0-9]+)", path)
    block = start.copy()
    facing = 0
    visited = []
    for res in reResult:
        if res[0] == "R":
            facing += 1
            facing %= 4
        else:
            facing -= 1
            if facing < 0:
                facing = 3
        if stopAtHQ:
            for i in range(int(res[1])):
                if facing == 0:
                    block[0] += 1
                elif facing == 1:
                    block[1] += 1
                elif facing == 2:
                    block[0] -= 1
                elif facing == 3:
                    block[1] -= 1
                if block in visited:
                    return manhattan_distance(start, block)
                visited.append(block.copy())
        else:
            if facing == 0:
                block[0] += int(res[1])
            elif facing == 1:
                block[1] += int(res[1])
            elif facing == 2:
                block[0] -= int(res[1])
            elif facing == 3:
                block[1] -= int(res[1])
    return manhattan_distance(start, block)


def part1(data, test=False) -> str:
    data = data[0]
    return str(followPath(data))


def part2(data, test=False) -> str:
    data = data[0]
    return str(followPath(data, True))
