import re

IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6

LAYER_SIZE = IMAGE_WIDTH * IMAGE_HEIGHT


def part1(data, test=False) -> str:
    reFind = re.findall(".{" + str(LAYER_SIZE) + "}", data[0])
    min0 = -1
    result = 0

    for i in reFind:
        find0 = re.findall("0", i)
        find1 = re.findall("1", i)
        find2 = re.findall("2", i)

        if min0 > len(find0) or min0 == -1:
            min0 = len(find0)
            result = len(find1) * len(find2)

    return result


def part2(data, test=False) -> str:
    reFind = re.findall(".{" + str(LAYER_SIZE) + "}", data[0])

    result = ""

    for i in range(LAYER_SIZE):
        pixelFound = False
        for j in range(len(reFind)):
            if reFind[j][i] != "2":
                if reFind[j][i] == "0":
                    result += " "
                else:
                    result += "1"
                pixelFound = True
                break

        if not pixelFound:
            result += " "

    match = re.findall(".{" + str(IMAGE_WIDTH) + "}", result)

    for out in match:
        print(out)

    return "See Above"
