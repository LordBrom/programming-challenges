import re
import math


class RecipeDictionary():
    def __init__(self, data, debug=False):
        self.debug = debug
        self.dictionary = {}
        for d in data:
            newRecipe = Recipe(d, debug)
            self.dictionary[newRecipe.output[1]] = newRecipe

    def printDictionary(self):
        for r in self.dictionary:
            self.dictionary[r].printRecipe()

    def produceOutput(self, product):
        return self.dictionary[product[0]].produceAmount(self.dictionary, product[1])


class Recipe():
    def __init__(self, inLine, debug):
        self.debug = debug
        self.input = []
        self.output = []

        splitLine = inLine.split(" => ")
        reInStr = "([0-9]+) ([A-Z]+)"
        reInput = re.findall(reInStr, splitLine[0])
        for i in reInput:
            self.input.append([int(i[0]), i[1]])

        reOutStr = "([0-9]+) ([A-Z]+)"
        reOutput = re.search(reOutStr, splitLine[1])

        self.output = [int(reOutput.group(1)), reOutput.group(2)]

    def printRecipe(self):
        outStr = ""

        first = True
        for r in self.input:
            if not first:
                outStr += ", "
            outStr += str(r[0]) + " " + r[1]
            first = False
        outStr += " => "
        outStr += str(self.output[0]) + " " + self.output[1]

        print(outStr)

    def produceAmount(self, dictionary, amount, leftOvers={}, space=""):
        timesProduced = math.ceil(amount / self.output[0])
        self.debugPrint([space, "producing", amount, self.output[1]])

        self.debugPrint([space, "total before leftOvers", leftOvers])

        requirements = {}
        resultLeftOvers = {}
        newRequirements = {}
        for i in self.input:

            self.debugPrint([space, "needs", i[0] * timesProduced, i[1]])

            leftOversUsed = 0
            newLeftOvers = {}
            if i[1] == "ORE":
                newRequirements["ORE"] = i[0] * timesProduced
            else:
                inputNeeded = i[0] * timesProduced
                if i[1] in leftOvers and leftOvers[i[1]] != 0:
                    leftOversUsed = min(inputNeeded, leftOvers[i[1]])
                    inputNeeded -= leftOversUsed
                    leftOvers[i[1]] -= leftOversUsed
                    if not i[1] in resultLeftOvers:
                        resultLeftOvers[i[1]] = 0
                    resultLeftOvers[i[1]] -= leftOversUsed
                    self.debugPrint([space, "Using", leftOversUsed, "leftovers",
                                    leftOvers[i[1]], "leftovers remain"])

                if not i[1] in leftOvers:
                    leftOvers[i[1]] = 0

                if inputNeeded != 0:
                    newRequirements, newLeftOvers = dictionary[i[1]].produceAmount(
                        dictionary, inputNeeded, leftOvers.copy(), space + "  ")

                for l in newLeftOvers:
                    if not l in leftOvers:
                        leftOvers[l] = 0
                    if not l in resultLeftOvers:
                        resultLeftOvers[l] = 0
                    self.debugPrint(
                        [space, 'Adding', newLeftOvers[l], l, "to left overs"])
                    leftOvers[l] += newLeftOvers[l]
                    resultLeftOvers[l] += newLeftOvers[l]

            for r in newRequirements:
                if not r in requirements:
                    requirements[r] = 0
                requirements[r] += newRequirements[r]

        self.debugPrint([space, "total after leftOvers", leftOvers])

        if not self.output[1] in resultLeftOvers:
            resultLeftOvers[self.output[1]] = 0
        resultLeftOvers[self.output[1]
                        ] += (self.output[0] * timesProduced) - amount
        self.debugPrint([space, "needs", requirements, "with",
                        (self.output[0] * timesProduced) - amount, "left over"])
        self.debugPrint([space, "total after leftOvers",
                        leftOvers, resultLeftOvers])
        return requirements, resultLeftOvers

    def debugPrint(self, debugstr):
        if self.debug:
            outStr = ""
            for i in debugstr:
                outStr += str(i) + " "
            print(outStr)


def part1(data):
    recipeDictionary = RecipeDictionary(data)
    # recipeDictionary.printDictionary()
    result, leftOvers = recipeDictionary.produceOutput(["FUEL", 1])
    # print(leftOvers)
    return result["ORE"]


def part2(data):
    return "not implemented"
