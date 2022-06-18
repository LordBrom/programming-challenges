import sys


def hexToBin(hexStr):
    hexToBinKey = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }
    result = ""
    for l in hexStr:
        result += hexToBinKey[l]
    return result


class Packet:
    def __init__(self):
        self.version = None
        self.typeID = None
        self.literal = None
        self.lengthType = None
        self.subPackets = []

    def countVersions(self):
        result = self.version
        for sp in self.subPackets:
            result += sp.countVersions()

        return result

    def getValue(self):
        result = 0
        if self.typeID == 0:
            for sp in self.subPackets:
                result += sp.getValue()

        elif self.typeID == 1:
            result = 1
            for sp in self.subPackets:
                result *= sp.getValue()

        elif self.typeID == 2:
            result = sys.maxsize
            for sp in self.subPackets:
                result = min(result, sp.getValue())

        elif self.typeID == 3:
            result = 0
            for sp in self.subPackets:
                result = max(result, sp.getValue())

        elif self.typeID == 4:
            result = self.literal

        elif self.typeID == 5:
            if self.subPackets[0].getValue() > self.subPackets[1].getValue():
                result = 1
            else:
                result = 0

        elif self.typeID == 6:
            if self.subPackets[0].getValue() < self.subPackets[1].getValue():
                result = 1
            else:
                result = 0

        elif self.typeID == 7:
            if self.subPackets[0].getValue() == self.subPackets[1].getValue():
                result = 1
            else:
                result = 0

        return result


def parseLiteral(data, pos):
    result = ""
    index = pos
    keepGoing = "1"
    while keepGoing == "1":
        keepGoing = data[index]
        newPart = data[index + 1 : index + 5]
        result += newPart
        index += 5
    return (int(result, 2), index)


def parsePacket(data, pos=0):
    packet = Packet()
    packet.version = int(data[pos : pos + 3], 2)
    packet.typeID = int(data[pos + 3 : pos + 6], 2)
    pos += 6
    if packet.typeID == 4:
        packet.literal, pos = parseLiteral(data, pos)
    else:
        packet.lengthType = int(data[pos])
        pos += 1
        if packet.lengthType == 0:
            packetLength = int(data[pos : pos + 15], 2)
            pos += 15
            stopPos = pos + packetLength
            while pos < stopPos:
                newPacket, pos = parsePacket(data, pos)
                packet.subPackets.append(newPacket)
        else:
            packetCount = int(data[pos : pos + 11], 2)
            pos += 11
            for i in range(packetCount):
                newPacket, pos = parsePacket(data, pos)
                packet.subPackets.append(newPacket)

    return packet, pos


def part1(data, test=False) -> str:
    packet = parsePacket(hexToBin(data[0]))[0]
    return str(packet.countVersions())


def part2(data, test=False) -> str:
    packet = parsePacket(hexToBin(data[0]))[0]
    return str(packet.getValue())
