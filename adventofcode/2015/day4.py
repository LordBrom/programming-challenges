import hashlib


def checkHash(checkString, zeroCount=5):
    hashCheck = hashlib.md5(checkString.encode()).hexdigest()
    if len(hashCheck) < zeroCount + 1:
        return False
    return hashCheck[:zeroCount] == ("0" * zeroCount) and hashCheck[zeroCount].isnumeric()


def part1(data):
    result = 0
    while not checkHash(data + str(result)):
        result += 1
    return result


def part2(data):
    result = 0
    while not checkHash(data + str(result), 6):
        result += 1
    return result
