

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

    def doTwists(self, count=1):
        for i in range(count):
            for length in self.lengths:

                self.shift(self.position)
                self.reverse_portion(length)
                self.shift(self.position, False)

                self.position += length + self.skipSize
                self.position %= len(self.nums)
                self.skipSize += 1

    def shift(self, amount, forwards=True):
        if forwards:
            self.nums = self.nums[amount:] + self.nums[:amount]
        else:
            self.nums = self.nums[-amount:] + self.nums[:-amount]

    def reverse_portion(self, length):
        self.nums = self.nums[:length][::-1] + self.nums[length:]

    def checkSum(self):
        return self.nums[0] * self.nums[1]

    def dense_hash(self):
        result = []
        for i in range(16):
            s = i*16
            step = 0
            for j in range(s, s+16):
                step ^= self.nums[j]
            result.append(step)
        return result

    def final_hash(self):
        denseHash = self.dense_hash()

        result = ""
        for l in denseHash:
            if len(str(hex(l))[2:]) == 1:
                result += "0"
            result += str(hex(l))[2:]
        return result


def part1(data, test=False):
    length = 256
    if test:
        length = 5
    hashString = HashString(data, length)
    hashString.doTwists()
    return hashString.checkSum()


def part2(data, test=False):
    extraLengths = "17,31,73,47,23"
    lengths = ""
    if data == []:
        data = ""

    for char in data:
        lengths += str(ord(char)) + ","
    lengths += extraLengths

    hashString = HashString(lengths)
    hashString.doTwists(64)
    return hashString.final_hash()
