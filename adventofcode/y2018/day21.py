from y2018.TimeDevice import TimeDevice


def part1(data, test=False) -> str:
    insPointerSlot = int(data.pop(0).split(" ")[1])
    # only instruction 28 affects register 0
    # ran inputs until instruction 28 came up
    # it tried to compare 2884703 to register 0
    return str(
        TimeDevice(data, [2884703, 0, 0, 0, 0, 0], insPointerSlot).runInstructions()[0]
    )


def part2(data, test=False) -> str:
    insPointerSlot = int(data.pop(0).split(" ")[1])
    return str(TimeDevice(data, [0, 0, 0, 0, 0, 0], insPointerSlot).runInstructions())
