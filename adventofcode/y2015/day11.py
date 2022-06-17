def isValid(password):
    invalidChars = [ord("i") - 97, ord("o") - 97, ord("l") - 97]

    hasThreeConsecutive = False
    firstPair = None
    hasTwoPairs = False
    invalidChar = False

    for i in range(len(password)):
        if not hasThreeConsecutive and i < len(password) - 2:
            if (
                password[i] == password[i + 1] - 1
                and password[i] == password[i + 2] - 2
            ):
                hasThreeConsecutive = True

        if password[i] in invalidChars:
            invalidChar = True

        if not hasTwoPairs and i < len(password) - 1:
            if password[i] == password[i + 1]:
                if firstPair == None:
                    firstPair = i
                elif firstPair < i - 1:
                    hasTwoPairs = True

    return hasThreeConsecutive and not invalidChar and hasTwoPairs


def incrementPassword(password):
    index = -1
    password[index] += 1
    while password[index] >= 26:
        password[index] = 0
        index -= 1
        password[index] += 1
    return password


def passwordToNum(password):
    result = []
    for p in password:
        result.append(ord(p) - 97)
    return result


def numToPassword(num):
    result = ""
    for n in num:
        result += chr(n + 97)
    return result


def part1(data, test=False) -> str:
    startPassword = passwordToNum(data)
    password = incrementPassword(startPassword)
    while not isValid(password):
        password = incrementPassword(password)
    return numToPassword(password)


def part2(data, test=False) -> str:
    startPassword = passwordToNum(part1(data))
    password = incrementPassword(startPassword)
    while not isValid(password):
        password = incrementPassword(password)
    return numToPassword(password)
