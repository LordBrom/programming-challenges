import math


def solution(str):
    strLen = 0
    while strLen < (len(str) / 2) + 1:
        strLen += 1
        if math.ceil(len(str) / strLen) != int(len(str) / strLen):
            continue
        s = str[:strLen]

        con = False
        for i in range(int(len(str) / len(s))):
            if str[i * len(s):(i * len(s)) + len(s)] != s:
                con = True
                break

        if con:
            continue

        return int(len(str) / strLen)
