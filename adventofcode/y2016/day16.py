from tabnanny import check
from venv import create


def expandData(data):
    a = data
    ra = data[::-1]
    b = ""
    for l in ra:
        if l == "1":
            b += "0"
        else:
            b += "1"
    return a + "0" + b


def createChecksum(data):
    checksum = ""
    for i in range(0, len(data) - 1, 2):
        if data[i] == data[i + 1]:
            checksum += "1"
        else:
            checksum += "0"

    return checksum


def part1(data, test=False) -> str:
    diskSize = 272
    while len(data) < diskSize:
        data = expandData(data)
    checksum = createChecksum(data[:diskSize])
    while len(checksum) % 2 == 0:
        checksum = createChecksum(checksum)

    return checksum


def part2(data, test=False) -> str:
    diskSize = 35651584
    while len(data) < diskSize:
        data = expandData(data)
    checksum = createChecksum(data[:diskSize])
    while len(checksum) % 2 == 0:
        checksum = createChecksum(checksum)

    return checksum
