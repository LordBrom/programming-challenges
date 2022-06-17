from hashlib import md5


def getNextHash(data, index):
    result = ""
    while result[:5] != "00000":
        checkStr = data + str(index)
        result = md5(checkStr.encode()).hexdigest()
        index += 1
    return result, index


def part1(data, test=False) -> str:
    result = ""
    i = 0

    while len(result) < 8:
        hashCheck, i = getNextHash(data, i)
        result += hashCheck[5]

    return result


def part2(data, test=False) -> str:
    result = [None for x in range(8)]
    i = 0

    while None in result:
        hashCheck, i = getNextHash(data, i)
        if "0" <= hashCheck[5] < "8" and result[int(int(hashCheck[5]))] == None:
            result[int(int(hashCheck[5]))] = hashCheck[6]

    return "".join(result)
