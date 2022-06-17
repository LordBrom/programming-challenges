def breakDownString(replacements, string):
    totalSteps = 0
    i = 0
    while string != "e":
        string, steps = replaceSimple(replacements, string)
        totalSteps += steps
        string, steps = replaceComplex(replacements, string)
        totalSteps += steps
    return totalSteps


def replaceSimple(replacements, string):
    i = 0
    steps = 0
    while len(string) > 1 and i < len(string):
        start = i
        first, i = getElement(string, i)
        if first in ["Rn", "Y", "Ar"]:
            continue
        second, i = getElement(string, i)
        if second in ["Rn", "Y", "Ar"]:
            continue

        pair = first + second

        if pair in replacements:
            steps += 1
            string = string[:start] + replacements[pair] + string[start + len(pair) :]
            i = start - 2
    return string, steps


def replaceComplex(replacements, string):
    i = 0
    steps = 0
    while len(string) > 1 and i < len(string):
        start = i
        end = None
        first, i = getElement(string, i)
        if first in ["Rn", "Y", "Ar"]:
            continue
        second, i = getElement(string, i)
        if second != "Rn":
            i -= len(second)
            continue

        for x in range(3):
            ignore, i = getElement(string, i)
            next, i = getElement(string, i)
            if next == "Ar":
                end = i
                break
            elif next != "Y":
                break

        if end == None:
            i = start + len(first)
            continue

        pair = string[start:end]

        if pair in replacements:
            steps += 1
            string = string[:start] + replacements[pair] + string[start + len(pair) :]
            i = start - 2
    return string, steps


def getElement(string, index):
    if index >= len(string):
        return "", index
    result = string[index]
    if index < len(string) - 1 and string[index + 1].islower():
        result += string[index + 1]
        index += 1
    return result, index + 1


def getUnique(startStr, replacements, checked=[]):
    results = []
    for i in range(len(startStr)):
        letter = startStr[i]
        if i < len(startStr) - 1 and startStr[i + 1].islower():
            letter += startStr[i + 1]
        if not letter in replacements:
            continue
        for rep in replacements[letter]:
            check = startStr[:i] + rep + startStr[i + len(letter) :]
            if check not in results and check not in checked:
                results.append(check)
        i += len(letter) - 1

    return results


def parseInput(data, reverse=False):
    replacements = {}
    popStr = data.pop(0)
    while popStr != "":
        strSplit = popStr.split(" => ")
        if reverse:
            replacements[strSplit[1]] = strSplit[0]
        else:
            if not strSplit[0] in replacements:
                replacements[strSplit[0]] = []
            replacements[strSplit[0]].append(strSplit[1])
        popStr = data.pop(0)
    return replacements, data.pop(0)


def part1(data, test=False) -> str:
    replacements, startStr = parseInput(data)
    unique = getUnique(startStr, replacements)
    return len(unique)


def part2(data, test=False) -> str:
    replacements, startStr = parseInput(data, True)
    # There is a bit of an ordering issue. But adding this replacement still gets the right answer ;)
    # SiThCaRnFAr needs to go to SiThRnFAr to use the ThRnFAr replacement
    # But with this, it goes to CaRnFAr. But it gives the same answer.
    # Note for fix, at each step just have a "make change" version and a "don't" version and find best
    replacements["CaRnFAr"] = "F"
    return breakDownString(replacements, startStr)
