def has_duplicate_words(string):
    words = string.split(" ")
    setCheck = set(words)
    if len(setCheck) == len(words):
        return False
    return True


def has_anagram_words(string):
    words = string.split(" ")
    for i in range(len(words)):
        for ii in range(len(words)):
            if i == ii:
                continue
            if len(words[i]) != len(words[ii]):
                continue

            if count_letters(words[i]) == count_letters(words[ii]):
                return True
    return False


def count_letters(word):
    result = {}
    for l in word:
        if not l in result:
            result[l] = 0
        result[l] += 1

    return result


def part1(data, test=False) -> str:
    result = 0
    for d in data:
        if not has_duplicate_words(d):
            result += 1
    return result


def part2(data, test=False) -> str:
    result = 0
    for d in data:
        if has_duplicate_words(d):
            continue
        if has_anagram_words(d):
            continue
        result += 1
    return result
