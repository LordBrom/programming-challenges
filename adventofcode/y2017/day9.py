from gc import garbage


def find_closing_group(string, index):
    openCount = -1
    while string[index] != "}" or openCount > 0:
        if string[index] == "!":
            index += 1
        if string[index] == "<":
            index = find_closing_garbage(string, index)
        elif string[index] == "{":
            openCount += 1
        elif string[index] == "}":
            openCount -= 1
        index += 1
    return index


def find_closing_garbage(string, index):
    while string[index] != ">":
        if string[index] == "!":
            index += 1
        index += 1
    return index


def find_closing(string, index, type):
    if type == "{":
        return find_closing_group(string, index)
    elif type == "<":
        return find_closing_garbage(string, index)


def count_groups(string, groupVal=1):
    index = 0
    result = 0
    garbage = ""
    while index < len(string):
        start = index + 1
        if string[index] == "!":
            index += 1
        elif string[index] == "{":
            index = find_closing(string, index, string[index])
            newResult, newGarbage = count_groups(string[start:index], groupVal + 1)
            result += groupVal + newResult
            garbage += newGarbage

        elif string[index] == "<":
            index = find_closing(string, index, string[index])
            garbage += string[start:index]
        index += 1

    return result, garbage


def remove_escaped(string):
    result = ""

    i = 0
    while i < len(string):
        if string[i] == "!":
            i += 1
        else:
            result += string[i]
        i += 1

    return result


def part1(data, test=False) -> str:
    return str(count_groups(data)[0])


def part2(data, test=False) -> str:
    return str(len(remove_escaped(count_groups(data)[1])))
