import numpy as np


class TimeDevice():
    def __init__(self, instructionArray, startRegistry=[0, 0, 0, 0, 0, 0], instructionPointer=0) -> None:
        self.instructions = self.parseInstructions(instructionArray)
        self.registry = startRegistry
        self.ip = instructionPointer

    def runInstructions(self, getNum=False, debug=False):
        insNum = 0
        seen = []
        while True:
            if insNum >= len(self.instructions):
                break

            if debug:
                print("Current Registry: {}".format(self.registry))
                a, b, c = self.instructions[insNum][1]
                ins = self.instructions[insNum][0]
                print("run instruction: {} {} {} {} ({})".format(
                    ins, a, b, c, insNum))

            self.registry[self.ip] = insNum
            self.doOpcode(insNum, debug)

            if insNum == 28:
                if self.registry[5] in seen:
                    return seen[-1]
                seen.append(self.registry[5])

            if debug:
                print("After Registry: {}".format(self.registry))
                input()

            insNum = self.registry[self.ip]
            insNum += 1
            if getNum and self.registry[0] == 0:
                break
        return self.registry

    def doOpcode(self, instructionNum, debug=False):
        opCode = self.instructions[instructionNum][0]
        a, b, c = self.instructions[instructionNum][1]
        if opCode == "addr":
            if debug:
                print("add and {}, {} set to register {}".format(
                    self.registry[a], self.registry[b], c))
            self.registry[c] = self.registry[a] + self.registry[b]
        elif opCode == "addi":
            if debug:
                print("add and {}, {} set to register {}".format(
                    self.registry[a], b, c))
            self.registry[c] = self.registry[a] + b

        elif opCode == "mulr":
            if debug:
                print("multiply and {}, {} set to register {}".format(
                    self.registry[a], self.registry[b], c))
            self.registry[c] = self.registry[a] * self.registry[b]
        elif opCode == "muli":
            if debug:
                print("multiply and {}, {} set to register {}".format(
                    self.registry[a], b, c))
            self.registry[c] = self.registry[a] * b

        elif opCode == "banr":
            if debug:
                print("bit and {}, {} set to register {}".format(
                    self.registry[a], self.registry[b], c))
            self.registry[c] = self.registry[a] & self.registry[b]
        elif opCode == "bani":
            if debug:
                print("bit and {}, {} set to register {}".format(
                    self.registry[a], b, c))
            self.registry[c] = self.registry[a] & b

        elif opCode == "borr":
            if debug:
                print("bit or {}, {} set to register {}".format(
                    self.registry[a], self.registry[b], c))
            self.registry[c] = self.registry[a] | self.registry[b]
        elif opCode == "bori":
            if debug:
                print("bit or {}, {} set to register {}".format(
                    self.registry[a], b, c))
            self.registry[c] = self.registry[a] | b

        elif opCode == "setr":
            if debug:
                print("set {} to register {}".format(self.registry[a], c))
            self.registry[c] = self.registry[a]
        elif opCode == "seti":
            if debug:
                print("set {} to register {}".format(a, c))
            self.registry[c] = a

        elif opCode == "gtir":
            if a > self.registry[b]:
                if debug:
                    print("{} is gt {} set 1 to register {}".format(
                        a, self.registry[b], c))
                self.registry[c] = 1
            else:
                if debug:
                    print("{} is not gt {} set 0 to register {}".format(
                        a, self.registry[b], c))
                self.registry[c] = 0
        elif opCode == "gtri":
            if self.registry[a] > b:
                if debug:
                    print("{} is gt {} set 1 to register {}".format(
                        self.registry[a], b, c))
                self.registry[c] = 1
            else:
                if debug:
                    print("{} is not gt {} set 0 to register {}".format(
                        self.registry[a], b, c))
                self.registry[c] = 0
        elif opCode == "gtrr":
            if self.registry[a] > self.registry[b]:
                if debug:
                    print("{} is gt {} set 1 to register {}".format(
                        self.registry[a], self.registry[b], c))
                self.registry[c] = 1
            else:
                if debug:
                    print("{} is not gt {} set 0 to register {}".format(
                        self.registry[a], self.registry[b], c))
                self.registry[c] = 0

        elif opCode == "eqir":
            if a == self.registry[b]:
                if debug:
                    print("{} is equal {} set 1 to register {}".format(
                        a, self.registry[b], c))
                self.registry[c] = 1
            else:
                if debug:
                    print("{} is equal {} set 0 to register {}".format(
                        a, self.registry[b], c))
                self.registry[c] = 0
        elif opCode == "eqri":
            if self.registry[a] == b:
                if debug:
                    print("{} is equal {} set 1 to register {}".format(
                        self.registry[a], b, c))
                self.registry[c] = 1
            else:
                if debug:
                    print("{} is equal {} set 0 to register {}".format(
                        self.registry[a], b, c))
                self.registry[c] = 0
        elif opCode == "eqrr":
            if self.registry[a] == self.registry[b]:
                if debug:
                    print("{} is equal {} set 1 to register {}".format(
                        self.registry[a], self.registry[b], c))
                self.registry[c] = 1
            else:
                if debug:
                    print("{} is equal {} set 0 to register {}".format(
                        self.registry[a], self.registry[b], c))
                self.registry[c] = 0

    def parseInstructions(self, data):
        result = []
        for d in data:
            dSplit = d.split(" ")
            result.append([dSplit.pop(0), [int(x) for x in dSplit]])
        return result
