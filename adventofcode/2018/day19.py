from TimeDevice import TimeDevice


def part1(data):
    insPointerSlot = int(data.pop(0).split(" ")[1])
    return TimeDevice(data, [0, 0, 0, 0, 0, 0], insPointerSlot).runInstructions()[0]


def part2(data):
    insPointerSlot = int(data.pop(0).split(" ")[1])
    num = TimeDevice(data, [1, 0, 0, 0, 0, 0],
                     insPointerSlot).runInstructions(True)[2]

    result = 0
    for i in range(1, num + 1):
        if (num / i == int(num / i)):
            result += i
    return result
