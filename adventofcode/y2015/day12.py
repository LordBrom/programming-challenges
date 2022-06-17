import json


def sumNumbers(jsonObj, ignoreRed=False) -> int:
    result = 0
    if isinstance(jsonObj, dict):
        for key in jsonObj:
            if isinstance(jsonObj[key], int):
                result += jsonObj[key]
            if ignoreRed and isinstance(jsonObj[key], str) and jsonObj[key] == "red":
                return 0
            if isinstance(jsonObj[key], dict) or isinstance(jsonObj[key], list):
                result += sumNumbers(jsonObj[key], ignoreRed)
    if isinstance(jsonObj, list):
        for val in jsonObj:
            if isinstance(val, int):
                result += val
            if isinstance(val, dict) or isinstance(val, list):
                result += sumNumbers(val, ignoreRed)
    return result


def part1(data, test=False) -> str:
    data = data[0]
    jsonObj = json.loads(data)
    return str(sumNumbers(jsonObj))


def part2(data, test=False) -> str:
    data = data[0]
    jsonObj = json.loads(data)
    return str(sumNumbers(jsonObj, True))
