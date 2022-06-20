from typing import List, Dict

inFile = open("day15.in", "r").read().split("\n")
inFile.pop()

memory: Dict[int, int] = {}

nums: List[int] = []
for i, val in enumerate(inFile[0].split(",")):
    memory[int(val)] = i
    nums[i] = int(val)

turn = len(nums)
nextNum = 0

while turn < 30000000:
    lastNum = nums[-1:][0]

    if not lastNum in memory:
        lastSaid = turn - 1
    else:
        lastSaid = memory[lastNum]

    nextNum = (turn - 1) - lastSaid
    memory[lastNum] = turn - 1
    nums.append(nextNum)

    turn += 1

print(nums[-1:][0])
