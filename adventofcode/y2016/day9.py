def getDecompressedLength(string, once=True):
    if string.find(")") == -1:
        return len(string)
    total = 0

    index = 0
    while index < len(string):

        if string[index] == "(":
            openParentheses = index
            index = string.find(")", index)
            closeParentheses = index
            expandMarker = string[openParentheses + 1 : closeParentheses]
            expandSplit = expandMarker.split("x")
            expandString = string[index + 1 : index + int(expandSplit[0]) + 1]

            if once:
                expandLength = len(expandString)
            else:
                expandLength = getDecompressedLength(expandString, once)

            total += expandLength * int(expandSplit[1])

            index += int(expandSplit[0])
        else:
            total += 1
        index += 1

    return total


def part1(data, test=False) -> str:
    return getDecompressedLength(data)


def part2(data, test=False) -> str:
    return getDecompressedLength(data, False)
