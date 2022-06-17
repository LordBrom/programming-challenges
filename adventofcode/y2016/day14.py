from hashlib import md5


def hasRepeatingChar(string, count=3, findChar=None):
    for i in range(len(string) - count + 1):
        char = string[i]
        if findChar != None and findChar != char:
            continue
        found = True
        for j in range(1, count):
            if char != string[i + j]:
                found = False
                break
        if found:
            return True, char
    return False, None


def getNextHash(data, index, stretchCount=1, lookUp={}):
    result = ""
    foundChar = False
    char = None
    while True:
        result, lookUp = stretchHash(data, index, stretchCount, lookUp)
        foundChar, char = hasRepeatingChar(result)
        if foundChar:
            for m in range(1000):
                subResult, lookUp = stretchHash(
                    data, index + (m + 1), stretchCount, lookUp
                )
                if hasRepeatingChar(subResult, 5, char)[0]:
                    return result, index, lookUp
        index += 1


def stretchHash(string, index, count, lookUp):
    if index in lookUp:
        return lookUp[index], lookUp
    string = string + str(index)
    for c in range(count):
        string = md5((string).encode()).hexdigest()
    lookUp[index] = string
    return string, lookUp


def part1(data, test=False) -> str:
    i = -1
    lookUp = {}
    for n in range(64):
        i += 1
        hashString, i, lookUp = getNextHash(data, i, 1, lookUp)
    return str(i)


def part2(data, test=False) -> str:
    i = -1
    lookUp = {}
    for n in range(64):
        i += 1
        hashString, i, lookUp = getNextHash(data, i, 2017, lookUp)
    return str(i)


# 21074 - high
