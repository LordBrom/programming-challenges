from typing import List


class Port:
    def __init__(self, id: int, compA: int, compB: int) -> None:
        self.id = id
        self.compA = compA
        self.compB = compB
        self.connA: List[Port] = []
        self.connB: List[Port] = []
        self.usingA = True
        self.strength = compA + compB

    def __str__(self) -> str:
        return f"{self.compA}+{self.compB}"

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Port) and self.id == __o.id

    def check_port_connection(self, other: "Port") -> None:
        if other.compA == self.compA:
            self.connA.append(other)
            other.connA.append(self)
        elif other.compB == self.compA:
            self.connA.append(other)
            other.connB.append(self)

        if other.compB == self.compB:
            self.connB.append(other)
            other.connB.append(self)
        elif other.compA == self.compB:
            self.connB.append(other)
            other.connA.append(self)

    def get_strongest(self, usingA: bool = True, visited: List["Port"] = []):
        best = self.strength
        visited.append(self)
        if usingA:
            for p in self.connB:
                if p in visited:
                    continue
                newVisited = visited.copy()
                check = self.strength + p.get_strongest(
                    self.compB == p.compA, newVisited.copy()
                )
                best = max(best, check)
        else:
            for p in self.connA:
                if p in visited:
                    continue
                newVisited = visited.copy()
                check = self.strength + p.get_strongest(
                    self.compA == p.compA, newVisited.copy()
                )
                best = max(best, check)
        return best

    def get_longest(self, usingA: bool = True, visited: List["Port"] = []):
        bestLength = 0
        bestStrength = 0
        visited.append(self)

        if usingA:
            for p in self.connB:
                if p in visited:
                    continue

                checkLength, checkStrength = p.get_longest(
                    self.compB == p.compA, visited.copy()
                )
                if checkLength > bestLength or (
                    checkLength == bestLength and checkStrength > bestStrength
                ):
                    bestLength = checkLength
                    bestStrength = checkStrength
        else:

            for p in self.connA:
                if p in visited:
                    continue

                checkLength, checkStrength = p.get_longest(
                    self.compA == p.compA, visited.copy()
                )
                if checkLength > bestLength or (
                    checkLength == bestLength and checkStrength > bestStrength
                ):
                    bestLength = checkLength
                    bestStrength = checkStrength
        return bestLength + 1, bestStrength + self.strength


def parse_input(data) -> List[Port]:
    ports: List[Port] = []
    index = 0
    for d in data:
        inSplit = d.split("/")
        newPort = Port(index, int(inSplit[0]), int(inSplit[1]))
        for p in ports:
            p.check_port_connection(newPort)
        ports.append(newPort)
        index += 1

    return ports


def part1(data, test=False) -> str:
    ports = parse_input(data)
    result = 0
    for p in ports:
        if p.compA == 0:
            check = p.get_strongest(visited=[])
        elif p.compB == 0:
            check = p.get_strongest(False, visited=[])
        else:
            continue
        result = max(result, check)
    return str(result)


def part2(data, test=False) -> str:
    ports = parse_input(data)
    bestLength = 0
    bestStrength = 0
    for p in ports:
        if p.compA == 0:
            length, strength = p.get_longest(visited=[])
        elif p.compB == 0:
            length, strength = p.get_longest(False, visited=[])
        else:
            continue
        if length > bestLength or (length == bestLength and strength > bestStrength):
            bestLength = length
            bestStrength = strength
    return str(bestStrength)
