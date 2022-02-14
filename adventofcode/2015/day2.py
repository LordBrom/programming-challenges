
class Box():
    def __init__(self, inLine) -> None:
        data = inLine.split("x")
        self.length = int(data[0])
        self.width = int(data[1])
        self.height = int(data[2])

    def getNeededPaper(self):
        side1 = self.length * self.width
        side2 = self.width * self.height
        side3 = self.height * self.length
        smallest = min(side1, side2, side3)

        return (2 * side1) + (2 * side2) + (2 * side3) + smallest

    def getNeededRibbon(self):
        largest = max(self.length, self.width, self.height)
        wrap = ((2 * self.length) + (2 * self.width) +
                (2 * self.height) - (2 * largest))
        bow = self.length * self.width * self.height
        return wrap + bow


def makeBoxes(data):
    boxes = []
    for d in data:
        boxes.append(Box(d))
    return boxes


def part1(data):
    boxes = makeBoxes(data)
    result = 0
    for box in boxes:
        result += box.getNeededPaper()

    return result


def part2(data):
    boxes = makeBoxes(data)
    result = 0
    for box in boxes:
        result += box.getNeededRibbon()

    return result
