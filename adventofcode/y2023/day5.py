from typing import List

class SeedRange():
    def __init__(self, start, length) -> None:
        self.start = start
        self.end = start + (length - 1)
        self.moved = False

    def __str__(self) -> str:
        return str(self.start) + " " + str(self.end)

    def __lt__(self, __o: object) -> bool:
        return isinstance(__o, SeedRange) and self.start < __o.start

    def move_range(self, mapStart, mapRange, mapDestination):
        mapEnd = mapStart + (mapRange - 1)
        result = []

        if mapEnd < self.start:
            return ([], [self])

        if mapStart > self.end:
            return ([], [self])

        if self.start < mapStart:
            result.append(SeedRange(self.start, mapStart - self.start))
            self.start = mapStart

        if self.end > mapEnd:
            result.append(SeedRange(mapEnd + 1, (self.end) - mapEnd ))
            self.end = mapEnd

        length = self.end - self.start
        self.start = mapDestination + (self.start - mapStart)
        self.end = self.start + length

        return ([self], result)


def part1(data, test=False) -> str:
    seeds = [int(n) for n in data.pop(0).split(": ")[1].split(" ")]
    data.pop(0)

    for _ in range(7):
        data.pop(0)
        new_seeds = [-1 for _ in range(len(seeds))]
        while len(data) > 0 and data[0] != "":
            mapping = [int(n) for n in data.pop(0).split(" ")]
            for i,seed in enumerate(seeds):
                if mapping[1] <= seed and seed < mapping[1] + mapping[2]:
                    new_seeds[i] = mapping[0] + (seed - mapping[1])
        for i,n in enumerate(new_seeds):
            if n != -1:
                seeds[i] = n
        if len(data) > 0:
            data.pop(0)

    return str(min(seeds))

def part2(data, test=False) -> str:
    seedStr = data.pop(0).split(": ")[1]
    data.pop(0)
    seedsRanges = [int(n) for n in seedStr.split(" ")]
    seeds: List[SeedRange] = []
    while len(seedsRanges):
        seeds.append(SeedRange(seedsRanges[0], seedsRanges[1]))
        seedsRanges.pop(0)
        seedsRanges.pop(0)

    for _ in range(7):
        data.pop(0)
        moved_seeds = []

        while len(data) > 0 and data[0] != "":
            mapping = [int(n) for n in data.pop(0).split(" ")]
            recheck_seeds = []

            while len(seeds):
                seed = seeds.pop(0)
                moved, recheck = seed.move_range(mapping[1], mapping[2], mapping[0])

                if len(moved):
                    moved_seeds.append(moved[0])

                for check_seed in recheck:
                    recheck_seeds.append(check_seed)
            seeds = recheck_seeds

        for seed in moved_seeds:
            seeds.append(seed)

        if len(data) > 0:
            data.pop(0)

    seeds.sort()

    return str(seeds[0].start)
