

class HashKnot():
    def __init__(self, num) -> None:
        self.num = num
        pass


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
        input()
        for length in self.lengths:
            # print(self.position)
            start = self.position
            end = (start + length) % len(self.nums)
            if start < end:
                print(self.nums[:start],
                      "(", self.nums[start:end], ")", self.nums[end:])
                self.nums = self.nums[:start] + \
                    self.nums[start:end][::-1] + self.nums[end:]
            else:
                print(self.nums[:end], ")",
                      self.nums[end:start], "(",  self.nums[start:])

                self.nums = self.nums[start:][::-1] + \
                    self.nums[end:start] + self.nums[:end][::-1]
            self.position += length + self.skipSize
            self.position %= len(self.nums)
            self.skipSize += 1
            print(self)
            input()

    def checkSum(self):
        return self.nums[0] * self.nums[1]


def part1(data):
    hashString = HashString(data, 5)
    hashString.doTwists()
    return hashString.checkSum()


def part2(data):
    return "not implemented"
