def part1(data, test=False) -> str:
    result = 0
    for i in data:
        expecting = []
        errorCharFound = []
        for l in i:
            if l == "{":
                expecting.append("}")
            elif l == "[":
                expecting.append("]")
            elif l == "(":
                expecting.append(")")
            elif l == "<":
                expecting.append(">")
            elif l == "}" or l == "]" or l == ")" or l == ">":
                expect = expecting.pop()
                if l != expect:
                    if l == ")" and not ")" in errorCharFound:
                        errorCharFound.append(")")
                        result += 3
                    if l == "]" and not "]" in errorCharFound:
                        errorCharFound.append("]")
                        result += 57
                    if l == "}" and not "}" in errorCharFound:
                        errorCharFound.append("}")
                        result += 1197
                    if l == ">" and not ">" in errorCharFound:
                        errorCharFound.append(">")
                        result += 25137
    return result


def part2(data):
    resultScores = []
    for i in data:
        expecting = []
        for l in i:
            isValid = True
            if l == "{":
                expecting.append("}")
            elif l == "[":
                expecting.append("]")
            elif l == "(":
                expecting.append(")")
            elif l == "<":
                expecting.append(">")
            elif l == "}" or l == "]" or l == ")" or l == ">":
                expect = expecting.pop()
                if l != expect:
                    isValid = False
                    break
        if isValid:
            score = 0
            for e in expecting[::-1]:
                score *= 5
                if e == ")":
                    score += 1
                if e == "]":
                    score += 2
                if e == "}":
                    score += 3
                if e == ">":
                    score += 4
            resultScores.append(score)
    resultScores.sort()

    return resultScores[int((len(resultScores) - 1) / 2)]
