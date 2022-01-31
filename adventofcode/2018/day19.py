
def runInstructions(register, instructions, pointerSlot, getNum=False, debug=False):
    insPointer = 0
    while True:
        if insPointer >= len(instructions):
            break

        opCode = instructions[insPointer][0]
        pointers = instructions[insPointer][1]
        register[pointerSlot] = insPointer
        before = register.copy()

        register = doOpcode(register.copy(), opCode, pointers)

        if debug:
            print("ip={} {} {} {} {}".format(
                insPointer, before, instructions[insPointer][0], instructions[insPointer][1], register))
            input()

        insPointer = register[pointerSlot]
        insPointer += 1
        if getNum and register[0] == 0:
            break
    return register


def doOpcode(register, opcode, pointers):
    a, b, c = pointers
    if opcode == "addr":
        register[c] = register[a] + register[b]
    elif opcode == "addi":
        register[c] = register[a] + b

    elif opcode == "mulr":
        register[c] = register[a] * register[b]
    elif opcode == "muli":
        register[c] = register[a] * b

    elif opcode == "banr":
        register[c] = register[a] & register[b]
    elif opcode == "bani":
        register[c] = register[a] & b

    elif opcode == "borr":
        register[c] = register[a] | register[b]
    elif opcode == "bori":
        register[c] = register[a] | b

    elif opcode == "setr":
        register[c] = register[a]
    elif opcode == "seti":
        register[c] = a

    elif opcode == "gtir":
        if a > register[b]:
            register[c] = 1
        else:
            register[c] = 0
    elif opcode == "gtri":
        if register[a] > b:
            register[c] = 1
        else:
            register[c] = 0
    elif opcode == "gtrr":
        if register[a] > register[b]:
            register[c] = 1
        else:
            register[c] = 0

    elif opcode == "eqir":
        if a == register[b]:
            register[c] = 1
        else:
            register[c] = 0
    elif opcode == "eqri":
        if register[a] == b:
            register[c] = 1
        else:
            register[c] = 0
    elif opcode == "eqrr":
        if register[a] == register[b]:
            register[c] = 1
        else:
            register[c] = 0

    return register


def parseInstructions(data):
    result = []
    for d in data:
        dSplit = d.split(" ")
        result.append([dSplit.pop(0), [int(x) for x in dSplit]])
    return result


def part1(data):
    insPointerSlot = int(data.pop(0).split(" ")[1])
    return runInstructions([0, 0, 0, 0, 0, 0], parseInstructions(data), insPointerSlot)[0]


def part2(data):
    insPointerSlot = int(data.pop(0).split(" ")[1])
    num = runInstructions([1, 0, 0, 0, 0, 0],
                          parseInstructions(data), insPointerSlot, True)[2]

    result = 0
    for i in range(1, num + 1):
        if (num / i == int(num / i)):
            result += i
    return result
