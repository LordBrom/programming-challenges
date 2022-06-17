import json


def sumNumbers(jsonObj, ignoreRed=False):
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


def part1(data):
    jsonObj = json.loads(data)
    return sumNumbers(jsonObj)


def part2(data):
    jsonObj = json.loads(data)
    return sumNumbers(jsonObj, True)
