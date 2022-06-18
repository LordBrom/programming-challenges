def getCommonBit(inputs, bitNumb):
    zeroCount = 0
    oneCount = 0
    for i in inputs:
        if i[bitNumb] == "0":
            zeroCount += 1
        else:
            oneCount += 1
    return [zeroCount, oneCount]


def part1(data, test=False) -> str:

    gamma = ""
    epsilon = ""

    for b in range(len(data[0])):
        commonBit = getCommonBit(data, b)
        if commonBit[0] > commonBit[1]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return str(int(gamma, 2) * int(epsilon, 2))


def getOxy(inputs, num=0):
    if len(inputs) == 1:
        return inputs[0]

    commonBit = getCommonBit(inputs, num)
    nextBits = []
    for i in inputs:
        if commonBit[0] > commonBit[1]:
            if i[num] == "0":
                nextBits.append(i)
        else:
            if i[num] == "1":
                nextBits.append(i)

    return getOxy(nextBits, num + 1)


def getCoTwo(inputs, num=0):
    if len(inputs) == 1:
        return inputs[0]

    commonBit = getCommonBit(inputs, num)
    nextBits = []
    for i in inputs:
        if commonBit[1] < commonBit[0]:
            if i[num] == "1":
                nextBits.append(i)
        else:
            if i[num] == "0":
                nextBits.append(i)

    return getCoTwo(nextBits, num + 1)


def part2(data, test=False) -> str:
    return str(int(getOxy(data), 2) * int(getCoTwo(data), 2))
