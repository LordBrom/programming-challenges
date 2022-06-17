def countCharacters(string):
    string = string[1:-1]
    literal = 2
    memory = 0
    i = 0
    while i < len(string):
        char = string[i]
        if char != "\\":
            literal += 1
            memory += 1
        else:
            if string[i + 1] in ["\\", '"']:
                literal += 2
                memory += 1
                i += 1
            else:
                literal += 4
                memory += 1
                i += 3
        i += 1

    return literal, memory


def encode(string):
    result = ""
    for s in string:
        if s in ["\\", '"']:
            result += "\\"
        result += s
    return '"' + result + '"'


def part1(data, test=False) -> str:
    literalValue = 0
    memoryValue = 0
    for d in data:
        literal, memory = countCharacters(d)
        literalValue += literal
        memoryValue += memory
    return literalValue - memoryValue


def part2(data, test=False) -> str:
    literalValue = 0
    memoryValue = 0
    for d in data:
        literal, memory = countCharacters(encode(d))
        literalValue += literal
        memoryValue += memory
    return literalValue - memoryValue
