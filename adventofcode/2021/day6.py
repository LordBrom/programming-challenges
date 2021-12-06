

class Fish:
    def __init__(self, startTimer):
        self.timer = startTimer

    def age_day(self):
        if (self.timer == 0):
            self.timer = 6
            return True
        self.timer -= 1
        return False


def part1(input):
    fishes = []
    input = input[0].split(",")

    for i in input:
        fishes.append(Fish(int(i)))

    days = 80

    for d in range(days):
        newFish = []

        for f in fishes:
            if f.age_day():
                newFish.append(Fish(8))
        for nf in newFish:
            fishes.append(nf)

    return len(fishes)


def part2(input):
    fishTimer = [0 for x in range(9)]
    input = input[0].split(",")

    for i in input:
        fishTimer[int(i)] += 1

    days = 256

    for d in range(days):
        newFish = fishTimer[0]
        fishTimer[0] = fishTimer[1]
        fishTimer[1] = fishTimer[2]
        fishTimer[2] = fishTimer[3]
        fishTimer[3] = fishTimer[4]
        fishTimer[4] = fishTimer[5]
        fishTimer[5] = fishTimer[6]
        fishTimer[6] = fishTimer[7] + newFish
        fishTimer[7] = fishTimer[8]
        fishTimer[8] = newFish

    result = 0

    for x in fishTimer:
        result += x

    return result
