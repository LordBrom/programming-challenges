import sys


def main(args=None):
    day = input("Day: ")

    default = ' \n\
def part1(data, test=False): \n\
    return "not implemented" \n\
\n\
\n\
def part2(data, test=False): \n\
    return "not implemented" \n\
'
    mainPath = "day" + day + ".py"
    inputPath = "inputs/day" + day + ".in"
    testPath = "testInputs/day" + day + ".in"

    main = open(mainPath, "x")
    main.write(default)
    open(inputPath, "x")
    open(testPath, "x")


if __name__ == '__main__':
    main(sys.argv[1:])
