import re

RESTR_RIGHT = " ([a-g]+)"
RESTR_LEFT = "([a-g]+) "


def part1(input):
    result = 0
    for i in input:
        inParsed = i.split("|")
        reResult = re.findall(RESTR_RIGHT, inParsed[1])

        for r in reResult:
            if len(r) == 2 or len(r) == 3 or len(r) == 4 or len(r) == 7:
                result += 1

    return result


def check3(oneKey, str):
    for l in oneKey:
        if not l in str:
            return False
    return True


def check5(fourKey, str):
    count = 0
    for l in fourKey:
        if not l in str:
            count += 1
            if count > 1:
                return False
    return True


def check6(sevenKey, str):
    for l in sevenKey:
        if not l in str:
            return True
    return False


def check9(threeKey, str):
    for l in threeKey:
        if not l in str:
            return False
    return True


def part2(input):
    result = 0
    count = 0
    for i in input:
        count += 1
        inParsed = i.split("|")
        leftSide = sorted(re.findall(RESTR_LEFT, inParsed[0]), key=len)
        rightSide = re.findall(RESTR_RIGHT, inParsed[1])

        numKey = ["" for x in range(10)]

        numKey[1] = leftSide[0]
        numKey[7] = leftSide[1]
        numKey[4] = leftSide[2]
        numKey[8] = leftSide[9]

        if check3(numKey[1], leftSide[3]):
            numKey[3] = leftSide[3]
        elif check3(numKey[1], leftSide[4]):
            numKey[3] = leftSide[4]
        elif check3(numKey[1], leftSide[5]):
            numKey[3] = leftSide[5]

        if numKey[3] != leftSide[3] and check5(numKey[4], leftSide[3]):
            numKey[5] = leftSide[3]
        elif numKey[3] != leftSide[4] and check5(numKey[4], leftSide[4]):
            numKey[5] = leftSide[4]
        elif numKey[3] != leftSide[5] and check5(numKey[4], leftSide[5]):
            numKey[5] = leftSide[5]

        if numKey[3] != leftSide[3] and numKey[5] != leftSide[3]:
            numKey[2] = leftSide[3]
        elif numKey[3] != leftSide[4] and numKey[5] != leftSide[4]:
            numKey[2] = leftSide[4]
        elif numKey[3] != leftSide[5] and numKey[5] != leftSide[5]:
            numKey[2] = leftSide[5]

        if check6(numKey[7], leftSide[6]):
            numKey[6] = leftSide[6]
        elif check6(numKey[7], leftSide[7]):
            numKey[6] = leftSide[7]
        elif check6(numKey[7], leftSide[8]):
            numKey[6] = leftSide[8]

        if numKey[6] != leftSide[6] and check9(numKey[3], leftSide[6]):
            numKey[9] = leftSide[6]
        elif numKey[6] != leftSide[7] and check9(numKey[3], leftSide[7]):
            numKey[9] = leftSide[7]
        elif numKey[6] != leftSide[8] and check9(numKey[3], leftSide[8]):
            numKey[9] = leftSide[8]

        if numKey[6] != leftSide[6] and numKey[9] != leftSide[6]:
            numKey[0] = leftSide[6]
        elif numKey[6] != leftSide[7] and numKey[9] != leftSide[7]:
            numKey[0] = leftSide[7]
        elif numKey[6] != leftSide[8] and numKey[9] != leftSide[8]:
            numKey[0] = leftSide[8]

        num = 0
        numStr = ""
        for n in range(len(rightSide)):
            for k in range(len(numKey)):
                if sorted(numKey[k]) == sorted(rightSide[n]):
                    if n == 0:
                        num += k * 1000
                        numStr += str(k)

                    elif n == 1:
                        num += k * 100
                        numStr += str(k)

                    elif n == 2:
                        num += k * 10
                        numStr += str(k)

                    elif n == 3:
                        num += k * 1
                        numStr += str(k)
                    break
        result += num

    return result
