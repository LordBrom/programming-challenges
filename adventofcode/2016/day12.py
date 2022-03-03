
class Computer():
    def __init__(self, instructions, cVal=0) -> None:
        self.registers = {
            'a': 0,
            'b': 0,
            'c': cVal,
            'd': 0
        }
        self.pointer = 0
        self.instructions = instructions

    def __str__(self) -> str:
        return "a: {}; b: {}; c: {}; d: {}; ".format(
            self.registers['a'], self.registers['b'],
            self.registers['c'], self.registers['d'])

    def runInstructions(self, debug=False):
        while self.pointer < len(self.instructions):
            instruction = self.instructions[self.pointer]
            if debug:
                print(self)
                print(self.pointer, instruction)
            splitInstructions = instruction.split(" ")
            action = splitInstructions[0]
            inpOne = splitInstructions[1]
            inpTwo = 0
            if len(splitInstructions) == 3:
                inpTwo = splitInstructions[2]

            if action == "cpy":
                if inpOne in ['a', 'b', 'c', 'd']:
                    self.registers[inpTwo] = self.registers[inpOne]
                else:
                    self.registers[inpTwo] = int(inpOne)
            elif action == "inc":
                self.registers[inpOne] += 1
            elif action == "dec":
                self.registers[inpOne] -= 1
            elif action == "jnz":
                zeroCheck = None
                if inpOne in ['a', 'b', 'c', 'd']:
                    zeroCheck = self.registers[inpOne]
                else:
                    zeroCheck = int(inpOne)

                if zeroCheck != 0:
                    self.pointer += int(inpTwo) - 1
            self.pointer += 1
            if debug:
                print(self)
                input()


def part1(data):
    comp = Computer(data)
    comp.runInstructions()
    return comp.registers['a']


def part2(data):
    comp = Computer(data, 1)
    comp.runInstructions()
    return comp.registers['a']
