

def getUniqueReversed(startStr, replacements, checked=[]):
    results = []
    for rep in replacements:
        if replacements[rep] == "e" and startStr != rep:
            continue
        pos = startStr.find(rep)
        while pos != -1:
            check = startStr[:pos] + replacements[rep] + \
                startStr[pos + len(rep):]
            if check not in results and check not in checked:
                results.append(check)
            pos = startStr.find(rep, pos+1)

    return results


def getUnique(startStr, replacements, checked=[]):
    results = []
    for i in range(len(startStr)):
        letter = startStr[i]
        if i < len(startStr) - 1 and startStr[i+1].islower():
            letter += startStr[i+1]
        if not letter in replacements:
            continue
        for rep in replacements[letter]:
            check = startStr[:i] + rep + startStr[i+len(letter):]
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


def part1(data):
    replacements, startStr = parseInput(data)
    unique = getUnique(startStr, replacements)
    return len(unique)


def part2(data):
    replacements, startStr = parseInput(data, True)
    endStr = "e"
    unique = [startStr]
    steps = 0
    while not endStr in unique:
        steps += 1
        nextUnique = []
        for str in unique:
            nextUnique.extend(getUniqueReversed(str, replacements, nextUnique))
        unique = nextUnique

    return steps
