from cmath import isnan


class SoundProgram:
    def __init__(self, instructions, pVal=0) -> None:
        self.registers = {"p": pVal}
        self.pVal = pVal
        self.instructions = instructions
        self.index = 0
        self.sound = None
        self.valuesSent = 0

        self.inQueue = []
        self.outQueue = None

    def __str__(self) -> str:
        return str(self.pVal) + ": " + str(self.registers)

    def run(self):
        while not self.do_instruction():
            self.index += 1
        return self.sound

    def do_instruction(self):
        if self.index >= len(self.instructions) or self.index < 0:
            return True

        inst = self.instructions[self.index].split(" ")
        action = inst[0]

        if not inst[1].lstrip("-").isnumeric() and not inst[1] in self.registers:
            self.registers[inst[1]] = 0

        if action == "snd":
            self.valuesSent += 1
            if self.outQueue != None:
                self.outQueue.append(self.get_value(inst[1]))
            self.sound = self.get_value(inst[1])

        elif action == "set":
            self.registers[inst[1]] = self.get_value(inst[2])

        elif action == "add":
            self.registers[inst[1]] += self.get_value(inst[2])

        elif action == "mul":
            self.registers[inst[1]] *= self.get_value(inst[2])

        elif action == "mod":
            self.registers[inst[1]] %= self.get_value(inst[2])

        elif action == "rcv":
            if len(self.inQueue) == 0:
                return True
            self.registers[inst[1]] = self.inQueue.pop(0)

        elif action == "jgz":
            if self.get_value(inst[1]) > 0:
                self.index += self.get_value(inst[2]) - 1
        return False

    def get_value(self, value):
        if value.lstrip("-").isnumeric():
            return int(value)
        else:
            return self.registers[value]

    def is_deadlock(self):
        return len(self.inQueue) == 0 and self.instructions[self.index][:3] == "rcv"


def part1(data, test=False) -> str:
    soundProgram = SoundProgram(data)
    return soundProgram.run()


def part2(data, test=False) -> str:
    soundProgram0 = SoundProgram(data, 0)
    soundProgram1 = SoundProgram(data, 1)
    soundProgram0.outQueue = soundProgram1.inQueue
    soundProgram1.outQueue = soundProgram0.inQueue

    while not soundProgram0.is_deadlock() or not soundProgram1.is_deadlock():
        soundProgram0.run()
        soundProgram1.run()

    return str(soundProgram1.valuesSent)
