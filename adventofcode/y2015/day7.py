import typing
import re


class Wire:
    def __init__(self, wireName: str, value: typing.Optional[int] = None) -> None:
        self.name: str = wireName
        self.value: typing.Optional[int] = value
        self.action: typing.Optional[str] = None
        self.wire1: typing.Optional[Wire] = None
        self.wire2: typing.Optional[Wire] = None

    def __str__(self) -> str:
        return "{}: {} {}".format(self.name, self.value, self.action)

    def getValue(self) -> int:
        if self.value == None:
            if self.action == "SET":
                self.value = self.wire1.getValue()
            elif self.action == "NOT":
                self.value = ~self.wire1.getValue()
            elif self.action == "AND":
                self.value = self.wire1.getValue() & self.wire2.getValue()
            elif self.action == "OR":
                self.value = self.wire1.getValue() | self.wire2.getValue()
            elif self.action == "LSHIFT":
                self.value = self.wire1.getValue() << self.wire2.getValue()
            elif self.action == "RSHIFT":
                self.value = self.wire1.getValue() >> self.wire2.getValue()
        return self.value


class CircuitBoard:
    def __init__(self) -> None:
        self.wires: typing.Dict[str, Wire] = {}

    def __str__(self) -> str:
        result = ""
        for wire in self.wires:
            result += "\n{}: {}".format(wire, self.wires[wire].getValue())
        return result

    def inputCommand(self, command):
        reStr = "(.+) -> (.+)"
        reResult = re.search(reStr, command)
        wire = reResult.group(2)
        lSide = reResult.group(1)
        lSideSplit = lSide.split(" ")
        if not wire in self.wires:
            self.wires[wire] = Wire(wire)

        if len(lSideSplit) == 1:
            self.wires[wire].action = "SET"
            self.wires[wire].wire1 = self.addWire(lSideSplit[0])

        elif len(lSideSplit) == 2:
            self.wires[wire].action = lSideSplit[0]
            self.wires[wire].wire1 = self.addWire(lSideSplit[1])

        elif len(lSideSplit) == 3:
            self.wires[wire].action = lSideSplit[1]
            self.wires[wire].wire1 = self.addWire(lSideSplit[0])
            self.wires[wire].wire2 = self.addWire(lSideSplit[2])

    def addWire(self, wireName):
        if wireName.isnumeric():
            return Wire("input", int(wireName))
        else:
            if not wireName in self.wires:
                self.wires[wireName] = Wire(wireName)
            return self.wires[wireName]

    def getWire(self, wire="a") -> str:
        if wire in self.wires:
            return str(self.wires[wire].getValue())
        return ""


def part1(data, test=False) -> str:
    circuitBoard = CircuitBoard()
    for d in data:
        circuitBoard.inputCommand(d)
    return circuitBoard.getWire()


def part2(data, test=False) -> str:
    newBValue = part1(data.copy())
    circuitBoard = CircuitBoard()
    for d in data:
        circuitBoard.inputCommand(d)
    circuitBoard.wires["b"].wire1.value = int(newBValue)
    return circuitBoard.getWire()
