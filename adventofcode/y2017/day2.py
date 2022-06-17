import sys


def part1(data, test=False) -> str:
    result = 0
    for row in data:
        row = row.replace("\t", " ")
        rowSplit = row.split(" ")
        maxNum = 0
        minNum = sys.maxsize
        for val in rowSplit:
            maxNum = max(maxNum, int(val))
            minNum = min(minNum, int(val))
        result += maxNum - minNum
    return str(result)


def part2(data, test=False) -> str:
    result = 0
    for row in data:
        row = row.replace("\t", " ")
        rowSplit = [int(x) for x in row.split(" ")]
        for val in rowSplit:
            for val2 in rowSplit:
                if val == val2:
                    continue
                if int(val / val2) == val / val2:
                    result += int(val / val2)
    return str(result)
