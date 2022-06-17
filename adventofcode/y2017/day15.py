from math import floor


class Generator():
    def __init__(self, start, factor, submitVal) -> None:
        self.product = start
        self.factor = factor
        self.submitVal = submitVal

    def __str__(self) -> str:
        return str(self.product).rjust(
            10)

    def produceValue(self, resProduct=2147483647, checkVal=False):
        self.product *= self.factor
        self.product %= resProduct
        return self.product % self.submitVal == 0

    def setNextValue(self):
        while not self.produceValue():
            pass


class Judge():
    def __init__(self, data, useQueue=False, debug=False) -> None:
        aVal = data[0].split(" ")[-1]
        bVal = data[1].split(" ")[-1]
        self.genA = Generator(int(aVal), 16807, 4)
        self.genB = Generator(int(bVal), 48271, 8)

        self.result = 0
        self.useQueue = useQueue
        self.queA = []
        self.queB = []
        self.debug = debug
        if self.debug:
            print("--Gen. A--  --Gen. B--")

    def step(self, pairs):
        checked = 0
        while True:
            if self.useQueue:
                self.genA.setNextValue()
                self.genB.setNextValue()
            else:
                self.genA.produceValue()
                self.genB.produceValue()

            if not self.useQueue and self.debug:
                print("{}  {}".format(self.genA, self.genB))

            if self.debug:
                print()
                print(bin(self.genA.product)[-16:])
                print(bin(self.genB.product)[-16:])
            checked += 1
            if bin(self.genA.product)[-16:] == bin(self.genB.product)[-16:]:
                self.result += 1
            if checked == pairs:
                return


def part1(data, test=False):
    judge = Judge(data)
    judge.step(40000000)
    return judge.result


def part2(data, test=False):
    judge = Judge(data, True)
    judge.step(5000000)
    return judge.result
