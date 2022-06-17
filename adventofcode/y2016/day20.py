
class IpBlockRange():
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return "Blocking {} to {}, ({} IPs blocked)".format(self.start, self.end, self.end - self.start)

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, IpBlockRange) and self.start == __o.start and self.end == __o.end

    def __lt__(self, __o: 'IpBlockRange') -> bool:
        return self.start < __o.start

    def checkRange(self, other: 'IpBlockRange'):
        if (self.start - 1) <= other.start <= (self.end + 1):
            self.end = max(self.end, other.end)
            return True
        if (self.start - 1) <= other.end <= (self.end + 1):
            self.start = max(self.start, other.start)
            return True
        return False


def proccessIpRanges(data):
    ipRanges = []
    for d in data:
        splitData = d.split("-")
        ipRanges.append(IpBlockRange(int(splitData[0]), int(splitData[1])))
    lastSize = 0
    ipRanges.sort()
    while lastSize != len(ipRanges):
        lastSize = len(ipRanges)
        x = 0
        while x < len(ipRanges):
            y = x
            while y < len(ipRanges) - 1:
                y += 1
                if x == y:
                    continue
                if ipRanges[x].checkRange(ipRanges[y]):
                    del ipRanges[y]
                    y -= 1
            x += 1
    return ipRanges


def part1(data):
    ipRanges = proccessIpRanges(data)
    return ipRanges[0].end + 1


def part2(data):
    maxIp = 4294967295
    ipRanges = proccessIpRanges(data)

    blockedCount = 0
    for ipRange in ipRanges:
        blockedCount += (ipRange.end - ipRange.start) + 1
    return (maxIp + 1) - blockedCount
