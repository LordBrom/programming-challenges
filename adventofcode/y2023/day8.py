
import re
from aoc import least_common_multiple

class MapNode():
    def __init__(self, name) -> None:
        self.name = name
        self.left = None
        self.right = None

def parse_map(data):
    instructions = data.pop(0)
    data.pop(0)
    mapNodes = {}
    re_str = "([a-zA-Z0-9]+) = \(([a-zA-Z0-9]+), ([a-zA-Z0-9]+)\)"
    for line in data:
        reResult = re.search(re_str, line)
        nodeName = reResult.group(1)
        leftName = reResult.group(2)
        rightName = reResult.group(3)
        if not nodeName in mapNodes:
            mapNodes[nodeName] = MapNode(nodeName)

        if not leftName in mapNodes:
            mapNodes[leftName] = MapNode(leftName)
        mapNodes[nodeName].left = mapNodes[leftName]

        if not rightName in mapNodes:
            mapNodes[rightName] = MapNode(rightName)
        mapNodes[nodeName].right = mapNodes[rightName]

    return instructions, mapNodes

def follow_path(nodes, path, start, part2 = False):
    currentNode: MapNode = nodes[start]
    steps = 0
    reachedEnd = False
    while not reachedEnd:
        for step in path:
            steps += 1
            if step == "L":
                currentNode = currentNode.left
            elif step == "R":
                currentNode = currentNode.right

            if part2 and currentNode.name[2] == "Z":
                reachedEnd = True
            elif currentNode.name == "ZZZ":
                reachedEnd = True

            if reachedEnd:
                break
    return steps


def part1(data, test=False) -> str:
    instructions, mapNodes = parse_map(data)
    steps = follow_path(mapNodes, instructions, "AAA", True)

    return str(steps)


def part2(data, test=False) -> str:
    instructions,mapNodes = parse_map(data)
    steps = []

    for node in mapNodes:
        if node[2] == "A":
            steps.append(follow_path(mapNodes, instructions, node, True))

    return str(least_common_multiple(steps))

