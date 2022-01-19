
OPCODES = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr",
           "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]

OPCODE_KEY = {}


class OpcodeSample():
    def __init__(self, before, instruction, after) -> None:
        self.before = [int(x) for x in before.split(", ")]
        self.after = [int(x) for x in after.split(", ")]
        self.instruction = [int(x) for x in instruction.split(" ")]
        self.possible = self.checkOpcodes()

    def __str__(self) -> str:
        result = "-----------------------------------"
        result += "\n" + "Before: " + str(self.before)
        result += "\n" + str(self.instruction)
        result += "\n" + "After:  " + str(self.after)
        result += "\n" + "-----------------------------------"
        return result

    def checkOpcodes(self, opcodes=OPCODES):
        result = []
        if self.instruction[0] in OPCODE_KEY:
            result.append(OPCODE_KEY[self.instruction[0]])
        else:
            for opcode in opcodes:
                check = doOpcode(self.before.copy(), opcode,
                                 self.instruction[1:])
                if check == self.after:
                    result.append(opcode)
        return result


def doOpcode(inData, opcode, pointers):
    a, b, c = pointers
    if opcode == "addr":
        inData[c] = inData[a] + inData[b]
    elif opcode == "addi":
        inData[c] = inData[a] + b

    elif opcode == "mulr":
        inData[c] = inData[a] * inData[b]
    elif opcode == "muli":
        inData[c] = inData[a] * b

    elif opcode == "banr":
        inData[c] = inData[a] & inData[b]
    elif opcode == "bani":
        inData[c] = inData[a] & b

    elif opcode == "borr":
        inData[c] = inData[a] | inData[b]
    elif opcode == "bori":
        inData[c] = inData[a] | b

    elif opcode == "setr":
        inData[c] = inData[a]
    elif opcode == "seti":
        inData[c] = a

    elif opcode == "gtir":
        if a > inData[b]:
            inData[c] = 1
        else:
            inData[c] = 0
    elif opcode == "gtri":
        if inData[a] > b:
            inData[c] = 1
        else:
            inData[c] = 0
    elif opcode == "gtrr":
        if inData[a] > inData[b]:
            inData[c] = 1
        else:
            inData[c] = 0

    elif opcode == "eqir":
        if a == inData[b]:
            inData[c] = 1
        else:
            inData[c] = 0
    elif opcode == "eqri":
        if inData[a] == b:
            inData[c] = 1
        else:
            inData[c] = 0
    elif opcode == "eqrr":
        if inData[a] == inData[b]:
            inData[c] = 1
        else:
            inData[c] = 0

    return inData


def parseInput(data):
    firstPart = True
    samples = []
    run = True
    while run:
        if data[0] == "":
            break
        if firstPart:
            samples.append(OpcodeSample(
                data.pop(0)[9:-1], data.pop(0), data.pop(0)[9:-1]))
            if len(data) == 0:
                break
            data.pop(0)
    data.pop(0)
    data.pop(0)
    data.pop(0)

    return samples, data


def part1(data):
    samples = parseInput(data)[0]
    result = 0
    for s in samples:
        #print(s.instruction[0], s.possible)
        if len(s.possible) >= 3:
            result += 1
    return result


def part2(data):
    samples, final = parseInput(data)
    neededOpcodes = OPCODES.copy()
    while len(neededOpcodes) > 0:
        for s in samples:
            if not s.instruction[0] in OPCODE_KEY:
                check = s.checkOpcodes(neededOpcodes)
                if len(check) == 1:
                    OPCODE_KEY[s.instruction[0]] = check[0]
                    neededOpcodes.remove(check[0])

    start = [0, 0, 0, 0]
    for d in final:
        inst = [int(x) for x in d.split(" ")]
        start = doOpcode(start, OPCODE_KEY[inst[0]], inst[1:])
    return start[0]
