
def iterateString(string):
    result = ""

    start = 0
    while start < len(string):
        curChar = string[start]
        end = start + 1
        while end < len(string) and string[end] == curChar:
            end += 1
        result += str(end - start) + curChar
        start = end

    return result


def part1(data):
    string = data
    for i in range(40):
        string = iterateString(string)
    return len(string)


def part2(data):
    string = data
    for i in range(50):
        string = iterateString(string)
    return len(string)
