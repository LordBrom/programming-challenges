import day2 as Day


day = "2"

#inFile = open("testInputs/test1.in", "r").read().split("\n")
inFile = open("inputs/day" + day + ".in", "r").read().split("\n")
inFile.pop()


print("day" + day + " part1: " + str(Day.part1(inFile)))
print("day" + day + " part2: " + str(Day.part2(inFile)))
