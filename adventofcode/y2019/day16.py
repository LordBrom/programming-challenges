import math
from functools import lru_cache


class FlawedFrequencyTransmission:
    def __init__(self, data, pattern) -> None:
        self.transmission = data
        self.pattern = pattern
        self.step = 0

    def __str__(self) -> str:
        return str(self.step) + ": " + self.transmission

    def takeSteps(self, steps=100):
        for s in range(steps):
            self.takeStep()

    # @lru_cache(maxsize=None)
    def takeStep(self):
        newTransmission = ""
        for i in range(1, len(self.transmission) + 1):
            patternPointer = 1
            stepSum = 0
            for n in self.transmission:
                pos = math.floor((patternPointer % (len(self.pattern * i))) / i)
                stepSum += int(n) * self.pattern[pos]
                patternPointer += 1
            newTransmission += str(abs(stepSum) % 10)
        self.step += 1
        self.transmission = newTransmission


def part1(data, test=False) -> str:
    data = data[0]
    fft = FlawedFrequencyTransmission(data, [0, 1, 0, -1])
    fft.takeSteps()
    return fft.transmission[:8]


def part2(data, test=False) -> str:
    data = data[0]
    realMessage = ""
    for i in range(10000):
        realMessage += data
    offset = int(data[:7])
    fft = FlawedFrequencyTransmission(realMessage, [0, 1, 0, -1])
    fft.takeSteps()
    return fft.transmission[offset : offset + 8]
