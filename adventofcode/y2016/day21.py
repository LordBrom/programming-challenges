class Password:
    def __init__(self, startString, reverseScramble=False) -> None:
        self.string = startString
        self.reverseScramble = reverseScramble

    def __str__(self) -> str:
        return "".join(self.string)

    def swapPositions(self, x, y):
        if y < x:
            return self.swapPositions(y, x)
        self.string = (
            self.string[:x]
            + self.string[y]
            + self.string[x + 1 : y]
            + self.string[x]
            + self.string[y + 1 :]
        )

    def swapLetters(self, x, y):
        xPos = self.string.index(x)
        yPos = self.string.index(y)
        self.swapPositions(xPos, yPos)

    def rotate(self, right=True, steps=1):
        for n in range(steps):
            if not right == self.reverseScramble:
                self.string = self.string[-1] + self.string[:-1]
            else:
                self.string = self.string[1:] + self.string[0]

    def rotateFromPosition(self, letter):
        pos = self.string.index(letter)
        if self.reverseScramble:
            if pos % 2 == 0:
                temp = pos - 2
                if temp < 0:
                    temp += len(self.string)
                temp += len(self.string)
                temp = int(temp / 2)
            else:
                temp = int((pos - 1) / 2)
            pos = temp

        if pos >= 4:
            pos += 1
        pos += 1
        self.rotate(steps=pos)

    def reverse(self, x, y):
        if y < x:
            return self.reverse(y, x)
        self.string = (
            self.string[:x] + self.string[x : y + 1][::-1] + self.string[y + 1 :]
        )

    def move(self, x, y, firstCall=True):
        if firstCall and self.reverseScramble:
            return self.move(y, x, False)
        removedLetter = self.string[x]
        self.string = self.string[:x] + self.string[x + 1 :]
        self.string = self.string[:y] + removedLetter + self.string[y:]

    def scramble(self, instructions):
        for instruction in instructions:
            insSplit = instruction.split(" ")

            if insSplit[0] == "swap":
                if insSplit[1] == "position":
                    self.swapPositions(int(insSplit[2]), int(insSplit[5]))

                else:
                    self.swapLetters(insSplit[2], insSplit[5])

            elif insSplit[0] == "reverse":
                self.reverse(int(insSplit[2]), int(insSplit[4]))

            elif insSplit[0] == "rotate":
                if insSplit[1] == "based":
                    self.rotateFromPosition(insSplit[6])
                else:
                    self.rotate(insSplit[1] == "right", int(insSplit[2]))

            elif insSplit[0] == "move":
                self.move(int(insSplit[2]), int(insSplit[5]))


def part1(data, test=False) -> str:
    password = Password("abcdefgh")
    password.scramble(data)
    return str(password)


def part2(data, test=False) -> str:
    password = Password("fbgdceah", True)
    password.scramble(data[::-1])
    return str(password)
