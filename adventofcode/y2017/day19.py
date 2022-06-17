UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class Tubes:
    def __init__(self, data) -> None:
        rowLen = 0
        for row in data:
            rowLen = max(rowLen, len(row))

        self.tubes = []
        for row in data:
            self.tubes.append([x for x in row])
            while len(self.tubes[-1]) < rowLen:
                self.tubes[-1].append(" ")

        self.pos = [0, 0]
        self.dir = DOWN
        for col in range(len(self.tubes[0])):
            if self.tubes[0][col] == "|":
                self.pos[1] = col
                break
        self.steps = 0

    def follow(self):
        result = ""
        while True:
            current = self.tubes[self.pos[0]][self.pos[1]]
            if current == " ":
                break
            self.steps += 1

            if not current in ["|", "-", "+"]:
                result += current
            elif current == "+":
                if self.dir in [UP, DOWN]:
                    if not self.tubes[self.pos[0]][self.pos[1] - 1] in ["|", " "]:
                        self.dir = LEFT
                    else:
                        self.dir = RIGHT
                else:
                    if not self.tubes[self.pos[0] - 1][self.pos[1]] in ["-", " "]:
                        self.dir = UP
                    else:
                        self.dir = DOWN

            if self.dir == UP:
                self.pos[0] -= 1
            elif self.dir == RIGHT:
                self.pos[1] += 1
            elif self.dir == DOWN:
                self.pos[0] += 1
            elif self.dir == LEFT:
                self.pos[1] -= 1

        return result


def part1(data, test=False) -> str:
    tubes = Tubes(data)
    return tubes.follow()


def part2(data, test=False) -> str:
    tubes = Tubes(data)
    tubes.follow()
    return str(tubes.steps)
