import typing
import sys
import time
from importlib import import_module

OUTPUT = ""


def run_all() -> None:
    for y in range(2021, 2022):
        global OUTPUT
        OUTPUT = "y" + str(y) + "/output.txt"
        file = open(OUTPUT, "w")
        file.write("")
        file.close()

        printHorizontalLine()
        printHorizontalLine()
        printLine("| year {} {} |".format(y, " " * 67))
        printHorizontalLine()
        printLine("| {} | Answer{} | Run Time{} |".format(" " * 6, " " * 44, " " * 7))
        printHorizontalLine()
        if y == 2020:
            continue

        for d in range(1, 26):
            run_day(str(y), str(d), continuous=True)


def outputAnswer(part, answer, time):
    # print(answer)
    timeStr = str("{:,.0f}".format(time)) + " ms"
    try:
        printLine(
            "| Part {} | {} | {} |{}".format(
                part,
                answer.ljust(50, " "),
                timeStr.rjust(15, " "),
                "" if time < 60000 else " :C",
            )
        )
    except:
        printLine(
            "| Part {} | {} | {} |{}".format(
                part,
                "!!! NOT STRING !!!".ljust(50, " "),
                timeStr.rjust(15, " "),
                "" if time < 60000 else " :C",
            )
        )


def timeMs():
    return int(round(time.time() * 1000))


def printHorizontalLine():
    printLine("-" * 81)


def run_day(
    year: str,
    day: str,
    runTest: bool = False,
    runPart1: bool = True,
    continuous: bool = False,
) -> None:
    try:
        Day = import_module("y" + year + ".day" + day)
    except:
        return

    inFilePath = ""
    if runTest:
        inFilePath = "y" + year + "/testInputs/day" + day + ".in"
    else:
        inFilePath = "y" + year + "/inputs/day" + day + ".in"
    inFile = open(inFilePath, "r").read().split("\n")
    inFile.pop()

    if not continuous:
        printHorizontalLine()
    dayDsp = day
    if len(day) == 1:
        dayDsp += " "
    if continuous:
        printLine("| Day {} | {} | {} |".format(dayDsp, " " * 50, " " * 15))
    else:
        printLine(
            "| Day {} | Answer{} | Run Time{} |".format(dayDsp, " " * 44, " " * 7)
        )
    printHorizontalLine()

    if runPart1:
        run_part("1", Day.part1, inFile.copy(), runTest)

    run_part("2", Day.part2, inFile.copy(), runTest)


def run_part(
    part: str,
    dayPart: typing.Callable,
    inFile: typing.List[str],
    runTest: bool = False,
    continuous: bool = False,
) -> None:
    startTime = timeMs()
    answer = ""
    try:
        answer = dayPart(inFile.copy(), runTest)
    except KeyboardInterrupt:
        answer = "Interrupted"
    except:
        answer = "Failed"
    outputAnswer(part, answer, timeMs() - startTime)
    if not continuous:
        printHorizontalLine()


def printLine(line: str, toFile: bool = True):
    if toFile:
        global OUTPUT
        file = open(OUTPUT, "a")
        file.write(line + "\n")
        file.close()
    else:
        print(line)


def main(args=None) -> None:
    run_all()
    return
    year = "2016"
    day = "22"

    runTest = input("(1) Run test; (2/else) Run actual: ") == "1"
    runPart1 = input("Run part 1 (y)/else: ") == ""

    run_day(year, day, runTest, runPart1)


if __name__ == "__main__":
    main(sys.argv[1:])
