
class Debugger():
    def __init__(self, inStuff) -> None:
        self.registers = [int(x) for x in inStuff.split("	")]
        self.stateCheck = []

    def __str__(self) -> str:
        return str(self.registers)

    def run(self):
        steps = 0
        while not self.registers in self.stateCheck:
            self.stateCheck.append(self.registers.copy())
            steps += 1
            maxVal = max(self.registers)
            nextIndex = self.registers.index(maxVal)
            blockCount = self.registers[nextIndex]
            self.registers[nextIndex] = 0

            index = nextIndex + 1
            index %= len(self.registers)
            for i in range(blockCount):
                self.registers[index] += 1
                index += 1
                index %= len(self.registers)
        return steps


def part1(data):
    debugger = Debugger(data)
    return debugger.run()


def part2(data):
    debugger = Debugger(data)
    debugger.run()
    debugger.stateCheck = []
    return debugger.run()
