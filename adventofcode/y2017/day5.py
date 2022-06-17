class TrampolineMaze:
    def __init__(self, startState, part2=False) -> None:
        self.state = [int(x) for x in startState]
        self.index = 0
        self.steps = 0
        self.part2 = part2

    def __str__(self) -> str:
        return str(self.state)

    def take_step(self):
        movement = self.state[self.index]
        if self.part2 and movement >= 3:
            self.state[self.index] -= 1
        else:
            self.state[self.index] += 1
        self.index += movement
        self.steps += 1
        return self.index >= len(self.state)


def part1(data, test=False) -> str:
    maze = TrampolineMaze(data)
    while not maze.take_step():
        pass
    return maze.steps


def part2(data, test=False) -> str:
    maze = TrampolineMaze(data, True)
    while not maze.take_step():
        pass
    return maze.steps
