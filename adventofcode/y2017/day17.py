class SpinLock:
    def __init__(self, stepCount) -> None:
        self.currentPosition = 0
        self.numbers = [0]
        self.totalSteps = stepCount

    def __str__(self) -> str:
        result = ""
        for i in range(len(self.numbers)):
            if i == self.currentPosition:
                result += "(" + str(self.numbers[i]) + ") "
            else:
                result += " " + str(self.numbers[i]) + "  "
        return result

    def step(self):
        newPos = self.currentPosition + self.totalSteps
        newPos %= len(self.numbers)
        self.numbers.insert(newPos + 1, len(self.numbers))
        self.currentPosition = newPos + 1

    def result(self, part1=True):
        if part1:
            return self.numbers[self.currentPosition + 1]
        else:
            return self.numbers[1]


def part1(data, test=False) -> str:
    data = data[0]
    data = int(data)
    spinLock = SpinLock(data)
    for i in range(2017):
        spinLock.step()
    return str(spinLock.result())


def part2(data, test=False) -> str:
    data = data[0]
    data = int(data)

    oneNum = None
    index = 1
    position = 0
    numCount = 1
    for i in range(50000000):
        newPosition = ((position + data) % numCount) + 1
        if newPosition == 1:
            oneNum = index
        numCount += 1
        index += 1
        position = newPosition

    return str(oneNum)
