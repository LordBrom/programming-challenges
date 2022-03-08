import math
import collections


def bruteForcePart2(elfCount, debug=False):
    elfCount = int(elfCount)
    elves = list(range(1, elfCount + 1))
    index = -1

    while len(elves) > 1:
        index += 1
        if index >= len(elves):
            index = 0

        targetElf = index + math.floor(len(elves) / 2)
        targetElf %= len(elves)
        if debug:
            print("elf {} takes elf {}'s presents".format(
                elves[index], elves[targetElf]))
        del elves[targetElf]
        if targetElf < index:
            index -= 1
    return elves[0]


def bruteForcePart1(elfCount, debug=False):
    outElves = []
    index = -1
    if elfCount == 1:
        index += 1
    while len(outElves) < elfCount - 1:
        index += 1
        index %= elfCount
        if index in outElves:
            if debug:
                print("elf {} is out".format(index + 1))
            continue
        nextElf = index + 1
        nextElf %= elfCount
        while nextElf in outElves:
            nextElf += 1
            nextElf %= elfCount
        outElves.append((nextElf) % elfCount)
        if debug:
            print("elf {} takes elf {}'s presents".format(
                index + 1, (nextElf + 1)))
            input()
    return index + 1


def part1(data):
    binFormat = format(int(data), "b")
    large = "1" + ("0" * (len(binFormat) - 1))
    oneLarger = "1" + ("0" * (len(binFormat)))
    small = binFormat[1:]
    return int(oneLarger, 2) - (((int(large, 2) - int(small, 2)) * 2) - 1)


def part2(data):
    return bruteForcePart2(int(data))
