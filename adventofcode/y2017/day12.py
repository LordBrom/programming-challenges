from typing import List


class Program:
    def __init__(self, name) -> None:
        self.name = name
        self.connected: List[Program] = []
        self.groupNum = None

    def __str__(self) -> str:
        return "{} ({})".format(self.name, self.groupNum)

    def add_connection(self, connect):
        self.connected.append(connect)

    def get_connected(self, visited=None, groupNum=None):
        if visited == None:
            visited = []
        if groupNum != None:
            self.groupNum = groupNum
        for prog in self.connected:
            if not prog.name in visited:
                visited.append(prog.name)
                visited.extend(
                    [
                        x
                        for x in prog.get_connected(visited, groupNum)
                        if not x in visited
                    ]
                )
        return visited


def parse_input(data):
    programs = {}
    for d in data:
        d1 = d.split(" <-> ")
        d2 = d1[1].split(", ")

        if not d1[0] in programs:
            programs[d1[0]] = Program(d1[0])
        for prog in d2:
            if not prog in programs:
                programs[prog] = Program(prog)
            programs[d1[0]].add_connection(programs[prog])
    return programs


def part1(data, test=False) -> str:
    programs = parse_input(data)
    return str(len(programs["0"].get_connected()))


def part2(data, test=False) -> str:
    programs = parse_input(data)
    groupNum = 0
    for prog in programs:
        if programs[prog].groupNum == None:
            programs[prog].get_connected(groupNum=groupNum)
            groupNum += 1
    return str(groupNum)
