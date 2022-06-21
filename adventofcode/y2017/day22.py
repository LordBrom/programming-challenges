from sys import maxsize
from typing import List, Dict
from aoc import Point
import math
from copy import copy
from enum import Enum


class NodeState(Enum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3


class Node:
    def __init__(self, startState: NodeState = NodeState.CLEAN) -> None:
        self.state = startState

    def __str__(self) -> str:
        if self.state == NodeState.CLEAN:
            return "."
        if self.state == NodeState.WEAKENED:
            return "W"
        if self.state == NodeState.INFECTED:
            return "#"
        if self.state == NodeState.FLAGGED:
            return "F"
        return ""


class Virus:
    def __init__(self, infectedNodes: List[Point] = [], part1: bool = True) -> None:
        self.virusNodes: Dict[Point, Node] = {}
        self.position = Point(0, 0)
        self.direction = 0
        for node in infectedNodes:
            self.virusNodes[node] = Node(NodeState.INFECTED)
        self.virusBurst: int = 0
        self.dirPoints = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]
        self.part1 = part1

    def __str__(self) -> str:
        return f"pos: {self.position}; dir: {self.direction}"

    def check_node(self, point: Point):
        if not point in self.virusNodes:
            self.virusNodes[point] = Node()

    def turn(self, left: bool = False):
        if left:
            self.direction -= 1
            if self.direction < 0:
                self.direction = 3
        else:
            self.direction += 1
            self.direction %= 4

    def work_burst(self):
        self.check_node(copy(self.position))

        if self.virusNodes[self.position].state == NodeState.CLEAN:
            self.turn(left=True)
            if self.part1:
                self.virusNodes[self.position].state = NodeState.INFECTED
                self.virusBurst += 1
            else:
                self.virusNodes[self.position].state = NodeState.WEAKENED

        elif self.virusNodes[self.position].state == NodeState.WEAKENED:
            self.virusNodes[self.position].state = NodeState.INFECTED
            self.virusBurst += 1

        elif self.virusNodes[self.position].state == NodeState.INFECTED:
            self.turn()
            if self.part1:
                self.virusNodes[self.position].state = NodeState.CLEAN
            else:
                self.virusNodes[self.position].state = NodeState.FLAGGED

        elif self.virusNodes[self.position].state == NodeState.FLAGGED:
            self.turn()
            self.turn()
            self.virusNodes[self.position].state = NodeState.CLEAN
        else:
            print(self.virusNodes[self.position])

        self.position.add_point(self.dirPoints[self.direction])

    def print_virus(self):
        minMaxX = [maxsize, 0]
        minMaxY = [maxsize, 0]
        for point in self.virusNodes.keys():
            minMaxX[0] = min(minMaxX[0], point.x)
            minMaxX[1] = max(minMaxX[1], point.x)
            minMaxY[0] = min(minMaxY[0], point.y)
            minMaxY[1] = max(minMaxY[1], point.y)

        for y in reversed(range(minMaxY[0], minMaxY[1] + 1)):
            rowStr = ""
            for x in range(minMaxX[0], minMaxX[1] + 1):
                checkPoint = Point(x, y)
                pointStr = "."
                if checkPoint in self.virusNodes:
                    pointStr = str(self.virusNodes[checkPoint])
                if point == self.position:
                    rowStr += f"[{pointStr}]"
                else:
                    rowStr += f" {pointStr} "

            print(rowStr)


def setup_virus(data: List[str], part1: bool = True):
    startNodes = []
    offset = math.floor(len(data) / 2)
    for y, d in enumerate(data):
        for x, p in enumerate(d):
            if p == "#":
                startNodes.append(Point(x - offset, offset - y))

    return Virus(startNodes, part1)


def part1(data: List[str], test: bool = False) -> str:
    virus = setup_virus(data)
    for i in range(10000):
        virus.work_burst()
    return str(virus.virusBurst)


def part2(data: List[str], test: bool = False) -> str:
    virus = setup_virus(data, False)
    for i in range(10000000):
        virus.work_burst()
    return str(virus.virusBurst)
