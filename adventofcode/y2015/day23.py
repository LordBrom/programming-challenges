class Computer:
    def __init__(self, instructions, aVal=0) -> None:
        self.registers = {"a": aVal, "b": 0}
        self.pointer = 0
        self.instructions = instructions

    def __str__(self) -> str:
        return str(self.registers)

    def run(self):
        while self.pointer < len(self.instructions):
            instruction = self.instructions[self.pointer]
            action = instruction[:3]
            rest = instruction[4:]
            if action == "hlf":
                self.registers[rest] /= 2
                self.pointer += 1
            elif action == "tpl":
                self.registers[rest] *= 3
                self.pointer += 1
            elif action == "inc":
                self.registers[rest] += 1
                self.pointer += 1
            elif action == "jmp":
                self.jump(rest)
            elif action == "jie":
                s = rest.split(", ")
                register = s[0]
                jumpAmount = s[1]
                if self.registers[register] % 2 == 0:
                    self.jump(jumpAmount)
                else:
                    self.pointer += 1
            elif action == "jio":
                s = rest.split(", ")
                register = s[0]
                jumpAmount = s[1]
                if self.registers[register] == 1:
                    self.jump(jumpAmount)
                else:
                    self.pointer += 1

    def jump(self, amount):
        if amount[0] == "+":
            self.pointer += int(amount[1:])
        elif amount[0] == "-":
            self.pointer -= int(amount[1:])


def part1(data, test=False) -> str:
    comp = Computer(data)
    comp.run()
    return str(comp.registers["b"])


def part2(data, test=False) -> str:
    comp = Computer(data, 1)
    comp.run()
    return str(comp.registers["b"])
