from y2019.intcode import IntcodeComputer

BLACK = "0"
WHITE = "1"

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class PaintJob:
    def __init__(self, width=125, startColor=BLACK):
        self.botPosX = width // 2
        self.botPosY = width // 2
        self.botFace = 0
        self.paint = []
        self.painted = []

        for row in range(width):
            newRow = []
            for col in range(width):
                newRow.append(BLACK)
            self.paint.append(newRow)
        self.paint[self.botPosX][self.botPosY] = startColor

    def print_job(self, readable=True):
        for row in self.paint:
            if readable:
                outStr = ""
                for col in row:
                    if col == BLACK:
                        outStr += " "
                    else:
                        outStr += "0"
                print(outStr)
            else:
                print("".join(row))

    def turn_bot(self, dir):
        if dir == 0:
            self.botFace -= 1
            if self.botFace < 0:
                self.botFace = 3
        else:
            self.botFace += 1
            if self.botFace > 3:
                self.botFace = 0

    def start_job(self, intCode):
        comp = IntcodeComputer(intCode)
        while True:
            if not [self.botPosX, self.botPosY] in self.painted:
                self.painted.append([self.botPosX, self.botPosY])

            currColor = self.paint[self.botPosX][self.botPosY]
            res = comp.run(currColor, False)
            if len(res) == 0:
                return
            color = res[0]
            turn = res[1]
            self.paint[self.botPosX][self.botPosY] = str(color)

            self.turn_bot(turn)

            if self.botFace == 0:
                self.botPosX += 1
            elif self.botFace == 1:
                self.botPosY += 1
            elif self.botFace == 2:
                self.botPosX -= 1
            else:
                self.botPosY -= 1


def part1(data, test=False) -> str:
    paintJob = PaintJob()
    paintJob.start_job(data[0].split(","))
    return str(len(paintJob.painted))


def part2(data, test=False) -> str:
    paintJob = PaintJob(85, WHITE)
    paintJob.start_job(data[0].split(","))
    paintJob.print_job()
    return "See Above"
