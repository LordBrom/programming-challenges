import time
import day5 as Day

day = "5"

runTest = input("(1) Run test; (2/else) Run actual: ")
runPart1 = input("Run part 1 (y)/else: ")

if runTest == "1":
    inFile = open("inputs/day" + day + ".in", "r").read().split("\n")
else:
    inFile = open("testInputs/day" + day + ".in", "r").read().split("\n")
inFile.pop()

if len(inFile) == 1:
    inPart1 = inFile.copy()[0]
    inPart2 = inFile.copy()[0]
else:
    inPart1 = inFile.copy()
    inPart2 = inFile.copy()


def outputAnswer(part, answer, time):
    timeStr = str("{:,.0f}".format(time)) + " ms"
    print(
        "| Part {} | {} | {} |".format(
            part, answer.ljust(50, " "), timeStr.rjust(15, " ")
        )
    )


def timeMs():
    return int(round(time.time() * 1000))


def printLine():
    print("-" * 81)


printLine()
dayDsp = day
if len(day) == 1:
    dayDsp += " "
print("| Day {} | Answer{} | Run Time{} |".format(dayDsp, " " * 44, " " * 7))
printLine()

if runPart1 == "":
    startTime = timeMs()
    outputAnswer("1", str(Day.part1(inPart1)), timeMs() - startTime)
    printLine()

startTime = timeMs()
outputAnswer("2", str(Day.part2(inPart2)), timeMs() - startTime)
printLine()
