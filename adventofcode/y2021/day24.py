import math
import random


class ALU:
    def __init__(self) -> None:
        self.val = {"w": 0, "x": 0, "y": 0, "z": 0}

    def __str__(self) -> str:
        return str(self.val)

    def doThing(self, instruction, inVal=None):
        action = instruction[:3]
        restSplit = instruction[4:].split(" ")
        val1 = restSplit[0]
        val2 = 0
        if len(restSplit) == 2:
            val2 = restSplit[1]
        try:
            int(val2)
            val2IsNum = True
        except:
            val2IsNum = False
        if action == "inp":
            if inVal == None:
                newVal = input()
            else:
                newVal = int(inVal)
        elif action == "add":
            if val2IsNum:
                newVal = int(self.val[val1]) + int(val2)
            else:
                newVal = int(self.val[val1]) + int(self.val[val2])
        elif action == "mul":
            if val2IsNum:
                newVal = int(self.val[val1]) * int(val2)
            else:
                newVal = int(self.val[val1]) * int(self.val[val2])
        elif action == "div":
            if val2IsNum:
                tempVal = int(self.val[val1]) / int(val2)
            else:
                tempVal = int(self.val[val1]) / int(self.val[val2])
            if tempVal > 0:
                newVal = math.floor(tempVal)
            else:
                newVal = math.ceil(tempVal)
        elif action == "mod":
            if val2IsNum:
                newVal = int(self.val[val1]) % int(val2)
            else:
                newVal = int(self.val[val1]) % int(self.val[val2])
        elif action == "eql":
            if val2IsNum:
                check = int(self.val[val1]) == int(val2)
            else:
                check = int(self.val[val1]) == int(self.val[val2])
            if check:
                newVal = 1
            else:
                newVal = 0
        self.val[val1] = newVal


def checkNum(data, num):
    alu = ALU()
    index = 0
    for d in data:
        if d[:3] == "inp":
            alu.doThing(d, num[index])
            index += 1
        else:
            alu.doThing(d)
    return alu.val["z"]


CHECKED = []


def randModalNum():
    result = ""
    for i in range(14):

        result += str(random.randint(1, 9))
    if result in CHECKED:
        return randModalNum()
    CHECKED.append(result)
    return result


def part1(data, test=False) -> str:
    num = 99893999291969

    while True:
        if str(num).find("0") != -1:
            num -= 1
            continue
        checkVal = checkNum(data, str(num))
        if checkVal == 0:
            return num
        num -= 1
    return None


def part2(data, test=False) -> str:
    num = 34171911181210

    while True:
        if str(num).find("0") != -1:
            num += 1
            continue
        checkVal = checkNum(data, str(num))
        if checkVal == 0:
            return num
        num += 1
    return None
