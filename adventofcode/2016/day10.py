import re


class Bot():
    def __init__(self, name, num) -> None:
        self.name = name
        self.num = num
        self.low = None
        self.high = None
        self.lowGoesTo = None
        self.highGoesTo = None

    def __str__(self) -> str:
        return "{} {}: [{}, {}]".format(self.name, self.num, self.low, self.high)

    def addValue(self, newValue):
        if self.low == None:
            self.low = newValue
        elif newValue < self.low:
            self.high = self.low
            self.low = newValue
        else:
            self.high = newValue
        return

    def giveValues(self, findLow=-1, findHigh=-1):
        if self.low == None or self.high == None:
            return False, False

        found = False
        if self.low == findLow and self.high == findHigh:
            found = True

        if self.name == "output":
            return False, found

        self.lowGoesTo.addValue(self.low)
        self.highGoesTo.addValue(self.high)

        self.low = None
        self.high = None

        return True, found


def inputToBots(data):
    bots = {}

    valueReStr = "value ([0-9]+) goes to bot ([0-9]+)"
    giveReStr = "bot ([0-9]+) gives low to (output|bot) ([0-9]+) and high to (output|bot) ([0-9]+)"
    data.sort(reverse=True)

    for d in data:
        if d[0] == "v":
            reResult = re.search(valueReStr, d)
            value = reResult.group(1)
            bot = reResult.group(2)
            botName = "bot-" + bot
            if not botName in bots:
                bots[botName] = Bot("bot", bot)
            bots[botName].addValue(int(value))
        else:
            reResult = re.search(giveReStr, d)
            bot = reResult.group(1)
            lowTo = reResult.group(3)
            highTo = reResult.group(5)
            botName = "bot-" + bot
            lowToName = reResult.group(2) + "-" + lowTo
            highToName = reResult.group(4) + "-" + highTo
            if not botName in bots:
                bots[botName] = Bot("bot", bot)

            if not lowToName in bots:
                bots[lowToName] = Bot(reResult.group(2), lowTo)
            bots[botName].lowGoesTo = bots[lowToName]

            if not highToName in bots:
                bots[highToName] = Bot(reResult.group(4), highTo)
            bots[botName].highGoesTo = bots[highToName]
    return bots


def part1(data):
    findLow = 17
    findHigh = 61
    bots = inputToBots(data)

    result = None
    i = 0
    botNames = list(bots.keys())
    while i < len(botNames):
        botName = botNames[i]
        botRes = bots[botName].giveValues(findLow, findHigh)
        if botRes[1]:
            result = botName
            break
        if botRes[0]:
            i = 0
        else:
            i += 1

    return bots[result].num


def part2(data):
    bots = inputToBots(data)
    i = 0
    botNames = list(bots.keys())
    while i < len(botNames):
        botName = botNames[i]
        botRes = bots[botName].giveValues()
        if botRes[0]:
            i = 0
        else:
            i += 1

    return bots["output-0"].low * bots["output-1"].low * bots["output-2"].low
