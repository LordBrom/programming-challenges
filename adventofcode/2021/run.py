import time
import day7 as Day

day = "7"

runTest = input("(1) Run actual; (2/else) Run test: ")

runPart1 = input("Run part 1 (y)/else: ")

if runTest == "1":
    inFile = open("inputs/day" + day + ".in", "r").read().split("\n")
else:
    inFile = open("testInputs/test1.in", "r").read().split("\n")
inFile.pop()


def outputAnswer(part, answer, time):
    timeStr = str("{:,.0f}".format(time)) + " ms"
    print("| Part {} | {} | {} |".format(
        part, answer.ljust(50, " "), timeStr.ljust(30, " ")))


def timeMs():
    return int(round(time.time() * 1000))


print("-" * 96)
print("| Day {}  | Answer{} | Run Time{} |".format(day, " " * 44, " " * 22))
print("-" * 96)

if runPart1 == "":
    startTime = timeMs()
    outputAnswer("1", str(Day.part1(inFile.copy())), timeMs() - startTime)
    print("-" * 96)

startTime = timeMs()
outputAnswer("2", str(Day.part2(inFile.copy())), timeMs() - startTime)
print("-" * 96)
