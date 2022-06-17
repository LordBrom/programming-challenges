import sys


def isValidRoom(roomCode):
    roomName = roomCode.split("-")
    lastPart = roomName.pop()
    lastSplit = lastPart.split("[")
    sectorID = int(lastSplit[0])
    checksum = lastSplit[1][:-1]

    letterCount = {}
    for code in roomName:
        for letter in code:
            if not letter in letterCount:
                letterCount[letter] = 0
            letterCount[letter] += 1

    sumCounts = sorted(letterCount.items(), key=lambda x: (-x[1], x[0]))
    check = "".join([x[0] for x in sumCounts[:5]])
    return check == checksum, sectorID, roomName


def part1(data, test=False) -> str:
    result = 0
    for d in data:
        isValid, sectorID, n = isValidRoom(d)
        if isValid:
            result += sectorID
    return str(result)


def part2(data, test=False) -> str:
    a_offset = 97
    for d in data:
        isValid, sectorID, encryptedName = isValidRoom(d)
        if isValid:
            roomName = ""
            for part in encryptedName:
                for letter in part:
                    num = ord(letter) - a_offset
                    num += sectorID
                    num %= 26
                    num += a_offset
                    roomName += chr(num)
                roomName += " "
            if roomName.strip() == "northpole object storage":
                break
    return str(sectorID)
