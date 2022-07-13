from collections import deque
from typing import Deque, List, Dict, Tuple
import re


class State:
    def __init__(self, data: List[str], stateName: str) -> None:
        self.name = stateName
        self.valInstructions: Dict[int, List[str]] = {}
        valStr = "If the current value is ([0-9]):"
        writeStr = "Write the value ([0-9])."
        dirStr = "Move one slot to the (left|right)."
        nextStateStr = "Continue with state ([a-zA-Z])."
        while len(data) > 0:
            val = int(re.search(valStr, data.pop(0)).group(1))
            self.valInstructions[val] = []
            write = re.search(writeStr, data.pop(0)).group(1)
            dir = re.search(dirStr, data.pop(0)).group(1)
            nextState = re.search(nextStateStr, data.pop(0)).group(1)
            self.valInstructions[val].append(write)
            self.valInstructions[val].append(dir)
            self.valInstructions[val].append(nextState)

    def __str__(self) -> str:
        result = f"\nIn state {self.name}:"
        for val in self.valInstructions.keys():
            result += f"\n  If the current value is {val}:"
            result += f"\n    - Write the value {self.valInstructions[val][0]}."
            result += f"\n    - Move one slot to the {self.valInstructions[val][1]}."
            result += f"\n    - Continue with state {self.valInstructions[val][2]}."
            result += "\n"

        return result

    def process(self, que: Deque, pointer: int) -> Tuple:
        curVal = que[pointer]
        que[pointer] = int(self.valInstructions[curVal][0])
        if self.valInstructions[curVal][1] == "right":
            if pointer == len(que) - 1:
                que.append(0)
            pointer += 1
        elif self.valInstructions[curVal][1] == "left":
            if pointer == 0:
                que.appendleft(0)
            else:
                pointer -= 1

        return self.valInstructions[curVal][2], que, pointer


def parseInput(data: List[str]) -> Tuple:
    beginStr = "Begin in state ([a-zA-Z])."
    stepsStr = "Perform a diagnostic checksum after ([0-9]+) steps."
    startState = re.search(beginStr, data.pop(0)).group(1)
    steps = int(re.search(stepsStr, data.pop(0)).group(1))
    states: Dict[str, State] = {}

    while len(data) > 0:
        data.pop(0)
        stateName = re.search("In state ([a-zA-Z]):", data.pop(0)).group(1)
        instructions: List[str] = []
        while len(data) > 0 and data[0] != "":
            instructions.append(data.pop(0))
        states[stateName] = State(instructions, stateName)

    return startState, steps, states


def part1(data, test=False) -> str:
    states: List[State]
    startState, steps, states = parseInput(data)
    que: deque = deque([0])
    index = 0
    state = startState

    for step in range(steps):
        state, que, index = states[state].process(que, index)

    result = 0
    for val in que:
        result += val

    return str(result)


def part2(data, test=False) -> str:
    return "Merry Christmas"
