from copy import deepcopy


class SecurityLayer:
    def __init__(self, depth, range) -> None:
        self.depth = depth
        self.range = range
        self.scanning = 0
        self.scanUp = False

    def __str__(self) -> str:
        result = str(self.depth) + " "
        for i in range(self.range):
            if self.scanning == i:
                result += "[S] "
            else:
                result += "[ ] "
        return result

    def tick_time(self):
        if self.scanUp:
            self.scanning -= 1
            if self.scanning == 0:
                self.scanUp = False
        else:
            self.scanning += 1
            if self.scanning == self.range - 1:
                self.scanUp = True

    def caught_severity(self):
        return self.depth * self.range

    def reset(self):
        self.scanning = 0
        self.scanUp = False


class SecurityLayers:
    def __init__(self, data) -> None:
        self.layers = {}
        self.max = 0

        self.time = 0
        self.position = None
        self.result = 0
        self.caught = False

        for d in data:
            dSplit = d.split(": ")
            self.layers[int(dSplit[0])] = SecurityLayer(int(dSplit[0]), int(dSplit[1]))
            self.max = max(self.max, int(dSplit[0]))

    def __str__(self) -> str:
        result = "\nPicosecond {}:".format(self.time)
        for i in range(self.max + 1):
            result += "\n"
            if i == self.position:
                result += " * "
            else:
                result += "   "
            if i in self.layers:
                result += str(self.layers[i])
            else:
                result += str(i)
        return result

    def tick_time(self, move=True):
        self.time += 1

        if move:
            if self.position == None:
                self.position = 0
            else:
                self.position += 1

        caught = False

        if (
            self.position != None
            and self.position in self.layers
            and self.layers[self.position].scanning == 0
        ):
            self.result += self.layers[self.position].caught_severity()
            self.caught = True
            caught = True

        for i in self.layers:
            self.layers[i].tick_time()

        return caught

    def reset(self):
        self.time = 0
        self.position = None
        self.result = 0
        self.caught = False

        for i in self.layers:
            self.layers[i].reset()


def part1(data, test=False) -> str:
    securityLayers = SecurityLayers(data)
    for i in range(securityLayers.max + 1):
        securityLayers.tick_time()
    return securityLayers.result


def part2(data, test=False) -> str:
    securityLayers = SecurityLayers(data)

    while True:
        securityLayers.tick_time(False)
        securityLayers.tick_time(False)
        securityCopy = deepcopy(securityLayers)

        for i in range(securityLayers.max + 1):
            if securityCopy.tick_time(True):
                break

        if not securityCopy.caught:
            break

    return securityLayers.time
