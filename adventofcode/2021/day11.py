

def part1(data):
    octopi = []

    for i in data:
        octopi.append([int(char) for char in i])

    flashes = 0

    for i in range(100):
        flashingOctopi = []
        for x in range(len(octopi)):
            for y in range(len(octopi[x])):
                octopi[x][y] += 1
                if octopi[x][y] > 9:
                    flashingOctopi.append([x, y])

        octoIndex = 0
        while octoIndex < len(flashingOctopi):
            for x in range(flashingOctopi[octoIndex][0] - 1, flashingOctopi[octoIndex][0] + 2):
                for y in range(flashingOctopi[octoIndex][1] - 1, flashingOctopi[octoIndex][1] + 2):
                    if x == flashingOctopi[octoIndex][0] and y == flashingOctopi[octoIndex][1]:
                        continue
                    if x < 0 or x >= len(octopi):
                        continue
                    if y < 0 or y >= len(octopi[0]):
                        continue
                    octopi[x][y] += 1
                    if octopi[x][y] > 9 and not [x, y] in flashingOctopi:
                        flashingOctopi.append([x, y])
            octoIndex += 1

        flashes += len(flashingOctopi)

        for r in flashingOctopi:
            octopi[r[0]][r[1]] = 0

    return flashes


def part2(data):
    octopi = []

    for i in data:
        octopi.append([int(char) for char in i])

    step = 0

    while True:
        step += 1
        flashingOctopi = []
        for x in range(len(octopi)):
            for y in range(len(octopi[x])):
                octopi[x][y] += 1
                if octopi[x][y] > 9:
                    flashingOctopi.append([x, y])

        octoIndex = 0
        while octoIndex < len(flashingOctopi):
            for x in range(flashingOctopi[octoIndex][0] - 1, flashingOctopi[octoIndex][0] + 2):
                for y in range(flashingOctopi[octoIndex][1] - 1, flashingOctopi[octoIndex][1] + 2):
                    if x == flashingOctopi[octoIndex][0] and y == flashingOctopi[octoIndex][1]:
                        continue
                    if x < 0 or x >= len(octopi):
                        continue
                    if y < 0 or y >= len(octopi[0]):
                        continue
                    octopi[x][y] += 1
                    if octopi[x][y] > 9 and not [x, y] in flashingOctopi:
                        flashingOctopi.append([x, y])
            octoIndex += 1

        if len(flashingOctopi) == 100:
            break

        for r in flashingOctopi:
            octopi[r[0]][r[1]] = 0

    return step
