from collections import deque


class ProgramDance:
    def __init__(self, dancerCount=16) -> None:
        self.dancers = deque([chr(i + 97) for i in range(dancerCount)])

    def __str__(self) -> str:
        return "".join(self.dancers)

    def do_dance(self, danceSteps):
        danceSteps = danceSteps.split(",")

        for danceStep in danceSteps:
            stepType = danceStep[0]
            stepDetails = danceStep[1:]
            if stepType == "s":
                self.spin(int(stepDetails))
            elif stepType == "x":
                positions = stepDetails.split("/")
                self.exchange(int(positions[0]), int(positions[1]))
            elif stepType == "p":
                programs = stepDetails.split("/")
                self.partner(programs[0], programs[1])

    def spin(self, size):
        self.dancers.rotate(size)

    def exchange(self, posA, posB):
        self.dancers[posA], self.dancers[posB] = self.dancers[posB], self.dancers[posA]

    def partner(self, progA, progB):
        posA = self.dancers.index(progA)
        posB = self.dancers.index(progB)
        self.exchange(posA, posB)


def part1(data, test=False) -> str:
    if test:
        dance = ProgramDance(5)
    else:
        dance = ProgramDance()

    dance.do_dance(data)

    return str(dance)


def part2(data, test=False) -> str:
    dance = ProgramDance()
    danceTimes = 1000000000
    # doing the dance 42 times, brings you back to the original order
    for i in range(danceTimes % 42):
        dance.do_dance(data)
    return str(dance)
