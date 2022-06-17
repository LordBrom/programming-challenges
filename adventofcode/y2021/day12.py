import re


class CaveSystem:
    def __init__(self, paths):
        self.connections = {}
        self.fullPaths = []
        reSplit = "([a-zA-Z]+)-([a-zA-Z]+)"
        for p in paths:
            pathSplit = re.search(reSplit, p)
            cave1 = pathSplit.group(1)
            cave2 = pathSplit.group(2)
            if not cave1 in self.connections:
                self.connections[cave1] = []
            if not cave2 in self.connections:
                self.connections[cave2] = []
            self.connections[cave1].append(cave2)
            self.connections[cave2].append(cave1)

    def searchCaves(
        self, extraSmallSearch=False, cave="start", path=[], usedExtraSearch=False
    ):
        if cave == "start":
            path = []
        path.append(cave)

        if cave == "end":
            self.fullPaths.append(path.copy())
            return

        for connection in self.connections[cave]:
            if connection == "start":
                continue
            if connection.lower() == connection and connection in path:
                if (not extraSmallSearch) or usedExtraSearch == True:
                    continue
                elif extraSmallSearch and not usedExtraSearch:
                    self.searchCaves(extraSmallSearch, connection, path.copy(), True)
                    continue
            self.searchCaves(
                extraSmallSearch, connection, path.copy(), not not usedExtraSearch
            )
        return


def part1(data, test=False) -> str:
    caveSystem = CaveSystem(data.copy())
    caveSystem.searchCaves()
    return str(len(caveSystem.fullPaths)
)

def part2(data, test=False) -> str:
    caveSystem = CaveSystem(data.copy())
    caveSystem.searchCaves(True)
    return str(len(caveSystem.fullPaths)
)
