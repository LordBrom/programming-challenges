

class HashString():
    def __init__(self, lengths, hashSize=256) -> None:
        self.lengths = [int(x) for x in lengths.split(",")]
        self.nums = list(range(hashSize))
        self.skipSize = 0
        self.position = 0

    def __str__(self) -> str:
        result = ""
        for i in range(len(self.nums)):
            if i == self.position:
                result += "[{}]".format(self.nums[i])
            else:
                result += " {} ".format(self.nums[i])
        return result

    def doTwists(self):
        print(self)
        print()
        for length in self.lengths:
            start = self.position
            end = (start + length) % len(self.nums)

            self.reverse_portion(start, end)

            self.position += length + self.skipSize
            self.position %= len(self.nums)
            self.skipSize += 1
            print(self)
            input()

    def reverse_portion(self, start, end):
        if start < end:
            print(self.nums[:start],
                  "(", self.nums[start:end], ")", self.nums[end:])
            self.nums = self.nums[:start] + \
                self.nums[start:end][::-1] + self.nums[end:]
            return
        print(self.nums[:end], ")",
              self.nums[end:start], "(",  self.nums[start:])

        startPart = self.nums[start:]
        endPart = self.nums[:end][::-1]
        rest = self.nums[end:start]

        if len(endPart) < len(startPart):
            self.nums = startPart[:len(endPart)][::-1] + \
                rest + endPart + startPart[len(endPart):][::-1]
        # elif len(endPart) > len(startPart):
        #    self.nums = startPart[:len(endPart)][::-1] + \
        #        rest + endPart + startPart[len(endPart):][::-1]
        else:
            self.nums = startPart[::-1] + rest + endPart

    def checkSum(self):
        return self.nums[0] * self.nums[1]


def part1(data, test=False):
    length = 256
    if test:
        length = 5
    hashString = HashString(data, length)
    hashString.doTwists()
    return hashString.checkSum()


def part2(data, test=False):
    return "not implemented"
