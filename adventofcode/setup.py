import sys


def main(args=None):
    year = input("Year: ")
    day = input("Day: ")

    default = ' \n\
def part1(data, test=False) -> str: \n\
    return str("not implemented") \n\
\n\
\n\
def part2(data, test=False) -> str: \n\
    return str("not implemented") \n\
'
    mainPath = "y" + year + "/day" + day + ".py"
    inputPath = "y" + year + "/inputs/day" + day + ".in"
    testPath = "y" + year + "/testInputs/day" + day + ".in"

    main = open(mainPath, "x")
    main.write(default)
    open(inputPath, "x")
    open(testPath, "x")


if __name__ == "__main__":
    main(sys.argv[1:])
