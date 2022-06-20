PREAMBLE = 25


def is_valid(num, validNums):
    for i in validNums:
        for j in validNums:
            if i == j:
                continue
            if int(i) + int(j) == int(num):
                return True
    return False


def check_sum(desire, nums):
    count = 0
    for num in nums:
        count += num
    return count == desire


inFile = open("day9.in", "r").read().split("\n")
inFile.pop()

intFile = [int(x) for x in inFile]

numToFind = 0
maxNum = 0

for i in range(PREAMBLE, len(intFile)):
    nums = []
    for j in range(PREAMBLE):
        nums.append(intFile[(i - j) - 1])
    if not is_valid(intFile[i], nums):
        numToFind = intFile[i]
        maxNum = i


for i in range(len(intFile)):
    for j in range(i, maxNum):
        nums = intFile[i:j]

        if check_sum(numToFind, nums):
            nums.sort()
            print(nums[0] + nums[len(nums) - 1])
