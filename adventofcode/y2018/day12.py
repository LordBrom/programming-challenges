class PlantPots():
    def __init__(self, initial, stepKey) -> None:
        self.state = initial
        self.stepKey = stepKey
        self.zeroPot = 0
        pass

    def __str__(self) -> str:
        result = ""
        for i in range(max(0, 3 - self.zeroPot)):
            result += "."
        return result + self.state

    def takeStep(self):
        nextState = ""

        for i in range(-1, len(self.state) + 1):
            plantStr = self.makePlantStr(i)
            if plantStr in self.stepKey:
                nextStr = self.stepKey[plantStr]
                if nextStr == '#' or i >= 0:
                    nextState += self.stepKey[plantStr]
                    if i < 0:
                        self.zeroPot += 1
            elif i >= 0 and i < len(self.state):
                nextState += "."

        self.state = nextState

    def makePlantStr(self, pos):
        result = ""
        for i in range(-2, 3):
            p = pos + i
            if p < 0 or p >= len(self.state):
                result += "."
            else:
                result += self.state[p]
        return result

    def getResult(self):
        result = 0
        for i in range(len(self.state)):
            if self.state[i] == '#':
                result += i - self.zeroPot
        return result


def parseInput(data):
    initialState = data.pop(0).split(" ")[2]
    data.pop(0)
    key = {}
    for d in data:
        keyRow = d.split(" => ")
        key[keyRow[0]] = keyRow[1]
    return initialState, key


def part1(data):
    initial, stepKey = parseInput(data)
    plantPots = PlantPots(initial, stepKey)
    for i in range(20):
        plantPots.takeStep()
    return plantPots.getResult()


def part2(data):
    initial, stepKey = parseInput(data)
    plantPots = PlantPots(initial, stepKey)
    for i in range(100):
        lastResult = plantPots.getResult()
        plantPots.takeStep()
    currentResult = plantPots.getResult()

    return currentResult + ((50000000000 - 100) * (currentResult - lastResult))
