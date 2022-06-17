import re


def isNiceString(checkString, debug=False):
    if debug:
        print("---------------------")
        print(checkString)
    reVowel = "a|e|i|o|u"
    reBadStr = "ab|cd|pq|xy"

    reVowelResult = re.findall(reVowel, checkString)
    reBadStrResult = re.findall(reBadStr, checkString)

    hasDouble = False
    for i in range(len(checkString) - 1):
        if checkString[i] == checkString[i + 1]:
            hasDouble = True

    if debug and not len(reVowelResult) >= 3:
        print("Does not contain enough vowels")
    if debug and not hasDouble:
        print("Does not contain double letters")
    if debug and not len(reBadStrResult) == 0:
        print("Contains bad string")

    return len(reVowelResult) >= 3 and hasDouble and len(reBadStrResult) == 0


def isNiceStringPart2(checkString, debug=False):
    if debug:
        print("---------------------")
        print(checkString)

    rule1 = False
    rule2 = False
    foundPairs = {}
    for i in range(len(checkString) - 1):

        if i < len(checkString) - 2 and checkString[i] == checkString[i + 2]:
            rule2 = True
        pairStr = checkString[i] + checkString[i + 1]
        if pairStr in foundPairs and i > foundPairs[pairStr] + 1:
            rule1 = True
        elif not pairStr in foundPairs:
            foundPairs[pairStr] = i

    if debug and not rule1:
        print("Does not contain two pairs")
    if debug and not rule2:
        print("Does not contain two same letters, with annother in between")

    return rule1 and rule2


def part1(data, test=False) -> str:
    result = 0
    for d in data:
        if isNiceString(d):
            result += 1
    return str(result)


def part2(data, test=False) -> str:
    result = 0
    for d in data:
        if isNiceStringPart2(d):
            result += 1
    return str(result)
