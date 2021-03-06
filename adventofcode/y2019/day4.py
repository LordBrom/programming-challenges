def check_valid(num, usePart2Rule=False):
    # Rule 1: It is a six-digit number.
    if len(num) != 6:
        return False

    # Rule 4: Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
    if "".join(sorted(num)) != num:
        return False

    # Rule 2: The value is within the range given in your puzzle input. - given
    # Rule 3: Two adjacent digits are the same (like 22 in 122345).
    digitCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    doubleCount = 0
    for i in range(6):
        digitCount[int(num[i]) - 1] += 1
        if digitCount[int(num[i]) - 1] == 2:
            doubleCount += 1
        elif usePart2Rule and digitCount[int(num[i]) - 1] == 3:
            doubleCount -= 1

    if doubleCount == 0:
        return False
    return True


def part1(data, test=False) -> str:
    data = data[0].split("-")

    minRange = data[0]
    maxRange = data[1]

    count = 0
    for i in range(int(minRange), int(maxRange)):
        if check_valid(str(i)):
            count += 1

    return str(count)


def part2(data, test=False) -> str:
    data = data[0].split("-")

    minRange = data[0]
    maxRange = data[1]

    count = 0
    for i in range(int(minRange), int(maxRange)):
        if check_valid(str(i), True):
            count += 1

    return str(count)
