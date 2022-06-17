def decodeMessage(message, part1=True):
    letterCounts = [{} for x in range(len(message[0]))]
    for word in message:
        for i in range(len(word)):
            if not word[i] in letterCounts[i]:
                letterCounts[i][word[i]] = 0
            letterCounts[i][word[i]] += 1
    result = ""
    mod = -1
    if not part1:
        mod = 1

    for letterCount in letterCounts:
        result += sorted(list(letterCount.items()), key=lambda x: mod * x[1])[0][0]
    return result


def part1(data, test=False) -> str:
    return decodeMessage(data)


def part2(data, test=False) -> str:
    return decodeMessage(data, False)
