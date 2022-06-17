import re


def getAbaStrings(string: str) -> list:
    result = []

    for i in range(len(string) - 2):
        if string[i] == string[i + 2] and string[i] != string[i + 1]:
            result.append(string[i + 1] + string[i] + string[i + 1])

    return result


def hasBabString(string: str, babStrings: list) -> bool:
    for i in range(len(string) - 2):
        if string[i : i + 3] in babStrings:
            return True
    return False


def hasAbbaString(string: str) -> bool:
    for i in range(len(string) - 3):
        if (
            string[i] == string[i + 3]
            and string[i + 1] == string[i + 2]
            and string[i] != string[i + 2]
        ):
            return True
    return False


def supportsTLS(ipString: str) -> bool:
    reStr = "\[([a-z]+)\]"
    reResult = re.findall(reStr, ipString)

    for bracketString in reResult:
        if hasAbbaString(bracketString):
            return False

    nonBracketParts = re.sub(reStr, "|", ipString).split("|")
    for nonBracketPart in nonBracketParts:
        if hasAbbaString(nonBracketPart):
            return True

    return False


def supportsSSL(ipString: str) -> bool:
    reStr = "\[([a-z]+)\]"
    reResult = re.findall(reStr, ipString)
    babStrings = []

    for bracketString in reResult:
        babStrings.extend(getAbaStrings(bracketString))

    nonBracketParts = re.sub(reStr, "|", ipString).split("|")
    for nonBracketPart in nonBracketParts:
        if hasBabString(nonBracketPart, babStrings):
            return True

    return False


def part1(data, test=False) -> str:
    result = 0
    for ip in data:
        if supportsTLS(ip):
            result += 1
    return str(result)


def part2(data, test=False) -> str:
    result = 0
    for ip in data:
        if supportsSSL(ip):
            result += 1
    return str(result)
