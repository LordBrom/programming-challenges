# Used for days 12, 23, and 25

class Computer():
    def __init__(self, instructions, aVal=0, cVal=0) -> None:
        self.registers = {
            'a': aVal,
            'b': 0,
            'c': cVal,
            'd': 0
        }
        self.pointer = 0
        self.instructions = [ins.split(" ") for ins in instructions]
        self.clockSignal = None
        self.outCount = 1000

    def __str__(self) -> str:
        return "a: {}; b: {}; c: {}; d: {}; ".format(
            self.registers['a'], self.registers['b'],
            self.registers['c'], self.registers['d'])

    def runInstructions(self, debug=False):
        while self.pointer < len(self.instructions):
            instruction = self.instructions[self.pointer]
            action = instruction[0]
            inpOne = instruction[1]
            inpTwo = None
            if len(instruction) == 3:
                inpTwo = instruction[2]

            if debug and self.registers['d'] == 0:
                print(self)
                print(self.pointer, action, inpOne, inpTwo)

            if action == "cpy":
                self.copy(inpOne, inpTwo)
            elif action == "inc":
                self.increase(inpOne)
            elif action == "dec":
                self.decrease(inpOne)
            elif action == "jnz":
                self.jump_if_not_zero(inpOne, inpTwo)
            elif action == "tgl":
                self.toggle_instruction(inpOne)
            elif action == "out":
                if not self.out(inpOne):
                    return False
                if self.outCount <= 0:
                    return True

            self.pointer += 1

            if debug and self.registers['d'] == 0:
                print(self)
                input()

    def get_value(self, val):
        if val in ['a', 'b', 'c', 'd']:
            return self.registers[val]
        else:
            return int(val)

    def copy(self, inpOne, inpTwo):
        if inpTwo in ['a', 'b', 'c', 'd']:
            self.registers[inpTwo] = self.get_value(inpOne)

    def increase(self, inpOne):
        self.registers[inpOne] += 1

    def decrease(self, inpOne):
        self.registers[inpOne] -= 1

    def jump_if_not_zero(self, inpOne, inpTwo):
        zeroCheck = self.get_value(inpOne)
        offset = self.get_value(inpTwo)

        if zeroCheck != 0:
            self.pointer += offset - 1

    def toggle_instruction(self, inpOne):
        target = self.pointer + self.get_value(inpOne)

        if target < len(self.instructions):
            if len(self.instructions[target]) == 2:
                if self.instructions[target][0] == "inc":
                    self.instructions[target][0] = "dec"
                else:
                    self.instructions[target][0] = "inc"
            elif len(self.instructions[target]) == 3:
                if self.instructions[target][0] == "jnz":
                    self.instructions[target][0] = "cpy"
                else:
                    self.instructions[target][0] = "jnz"

    def out(self, inpOne):
        newSignal = self.get_value(inpOne)
        if self.clockSignal == newSignal:
            return False
        self.clockSignal = newSignal
        self.outCount -= 1
        return True
