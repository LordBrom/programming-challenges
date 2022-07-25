from y2019.intcode import IntcodeComputer
from typing import Dict, List


class Packet:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x} {self.y}"


class Computer(IntcodeComputer):
    def __init__(self, networkAddress, data) -> None:
        self.networkAddress = networkAddress
        super().__init__(data)
        super().run(self.networkAddress)
        self.comps: Dict[int, Computer] = {}
        self.inputInstructions: List[Packet] = []
        self.isIdle = False

    def run(self):
        if len(self.inputInstructions) == 0:
            self.isIdle = True
            outputs = super().run(-1, False)
        else:
            self.isIdle = False
            instructions = self.inputInstructions.pop(0)
            super().run(instructions.x, False)
            outputs = super().run(instructions.y, False)

        while len(outputs) > 0:
            if len(outputs) < 3:
                break
            target = outputs.pop(0)
            packetX = outputs.pop(0)
            packetY = outputs.pop(0)
            if target == 255:
                return True, Packet(packetX, packetY)
            self.comps[target].inputInstructions.append(Packet(packetX, packetY))
        return False, None


def setup_computers(data, count: int = 50):
    comps: Dict[int, Computer] = {}
    for i in range(count):
        comps[i] = Computer(i, data)

    for address in comps:
        comps[address].comps = comps

    return comps


def part1(data, test=False) -> str:
    comps = setup_computers(data[0].split(","))
    while True:
        for address in comps:
            check, result = comps[address].run()
            if check:
                return str(result.y)


def part2(data, test=False) -> str:
    comps = setup_computers(data[0].split(","))
    natVal = Packet(0, 0)
    sentNatVals = []
    while True:
        for address in comps:
            check, result = comps[address].run()
            if check:
                natVal = result
        allIdle = True
        for address in comps:
            if not comps[address].isIdle:
                allIdle = False
                break
        if allIdle:
            if natVal.y in sentNatVals:
                return str(natVal.y)
            sentNatVals.append(natVal.y)
            comps[0].inputInstructions.append(natVal)
