import re


class Node:
    def __init__(self, x, y, size, used) -> None:
        self.x = x
        self.y = y
        self.size = size
        self.used = used
        self.adjacent = []

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Node) and self.x == __o.x and self.y == __o.y

    def __str__(self) -> str:
        result = "\n"
        result += self.getInfo()
        if len(self.adjacent) != 0:
            # result += "\nAdjacent Nodes:"
            for node in self.adjacent:
                result += "\n   " + node.getInfo()
        return result

    def getInfo(self):
        return (
            "/dev/grid/node-x{:02d}-y{:02d}  {:02d}T  {:02d}T  {:02d}T  {:02d}%".format(
                self.x, self.y, self.size, self.used, self.avail(), self.usedPercent()
            )
        )

    def avail(self):
        return self.size - self.used

    def usedPercent(self):
        return int((self.used / self.size) * 100)

    def isViablePair(self, nodeB: "Node", adjacent=False):
        if self.used == 0:
            return False

        if self == nodeB:
            return False

        if adjacent and not nodeB in self.adjacent:
            return False

        return nodeB.avail() >= self.used


def setupNodes(data):
    data.pop(0)
    data.pop(0)
    nodes = []

    reStr = "/dev/grid/node-x([0-9]+)-y([0-9]+)[ ]+([0-9]+)T[ ]+([0-9]+)T[ ]+([0-9]+)T[ ]+([0-9]+)%"

    for d in data:
        reResult = re.search(reStr, d)
        x = int(reResult.group(1))
        y = int(reResult.group(2))
        size = int(reResult.group(3))
        used = int(reResult.group(4))

        if y == 0:
            if x != 0:
                nodes.append(newRow)
            newRow = []

        newRow.append(Node(x, y, size, used))
    nodes.append(newRow)

    for nodeX in range(len(nodes)):
        for nodeY in range(len(nodes[nodeX])):
            temp = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for difX, difY in temp:
                x = nodeX + difX
                y = nodeY + difY

                if x < 0 or y < 0 or x >= len(nodes) or y >= len(nodes[x]):
                    continue

                nodes[nodeX][nodeY].adjacent.append(nodes[x][y])

    return nodes


def printNodes(nodes):
    for y in range(len(nodes[0])):
        rowStr = ""
        if y != 0:
            print(splitRow)
        splitRow = ""

        for x in range(len(nodes)):
            if x != 0:
                rowStr += " - "
            rowStr += "{:03d}/{:03d}:{:03d}".format(
                nodes[x][y].used, nodes[x][y].size, nodes[x][y].avail()
            )
            splitRow += "   |          "
        print(rowStr)


def part1(data, test=False) -> str:

    nodes = []
    reStr = "/dev/grid/node-x([0-9]+)-y([0-9]+)[ ]+([0-9]+)T[ ]+([0-9]+)T[ ]+([0-9]+)T[ ]+([0-9]+)%"

    for d in data:
        reResult = re.search(reStr, d)
        if reResult == None:
            continue
        nodes.append(
            Node(
                int(reResult.group(1)),
                int(reResult.group(2)),
                int(reResult.group(3)),
                int(reResult.group(4)),
            )
        )

    result = 0
    for nodeA in nodes:
        for nodeB in nodes:
            if nodeA == nodeB:
                continue
            if nodeA.isViablePair(nodeB):
                result += 1

    return result


def part2(data, test=False) -> str:
    nodes = setupNodes(data)
    printNodes(nodes)
    return "not implemented"
