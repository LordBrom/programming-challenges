import day3 as Day


inFile = open("testInputs/test1.in", "r").read().split("\n")
inFile.pop()
# print(str(Day.part2(inFile)))

# exit()

day = "3"
inFile = open("inputs/day" + day + ".in", "r").read().split("\n")
inFile.pop()
print("day" + day + " part1: " + str(Day.part1(inFile)))
print("day" + day + " part2: " + str(Day.part2(inFile)))
