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

    def produceAmount(self, dictionary, amount, inventory={}, space=""):
        timesProduced = math.ceil(amount / self.output[0])
        self.debugPrint([space, "producing", amount, self.output[1]])
        self.debugPrint([space, "start inventory", inventory])

        requirements = {}
        newRequirements = {}
        for i in self.input:

            self.debugPrint([space, "needs", i[0] * timesProduced, i[1]])

            if i[1] == "ORE":
                newRequirements["ORE"] = i[0] * timesProduced
            else:
                inputNeeded = i[0] * timesProduced
                if i[1] in inventory and inventory[i[1]] != 0:
                    leftOversUsed = min(inputNeeded, inventory[i[1]])
                    inputNeeded -= leftOversUsed
                    inventory[i[1]] -= leftOversUsed
                    self.debugPrint([space, "Using", leftOversUsed, "from inventory",
                                    inventory[i[1]], "leftovers remain"])

                if inputNeeded != 0:
                    newRequirements, inventory = dictionary[i[1]].produceAmount(
                        dictionary, inputNeeded, inventory.copy(), space + "    ")

            for r in newRequirements:
                if not r in requirements:
                    requirements[r] = 0
                requirements[r] += newRequirements[r]

        if not self.output[1] in inventory:
            inventory[self.output[1]] = 0
        remainder = (self.output[0] * timesProduced) - amount
        inventory[self.output[1]] += remainder

        self.debugPrint([space, "needs", requirements, "with",
                        remainder, "left over"])

        self.debugPrint([space, "end inventory", inventory])

        return requirements, inventory

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

    def debugPrint(self, debugstr):
        if self.debug:
            outStr = ""
            for i in debugstr:
                outStr += str(i) + " "
            print(outStr)


def part1(data):
    recipeDictionary = RecipeDictionary(data, True)
    # recipeDictionary.printDictionary()
    result, leftOvers = recipeDictionary.produceOutput(["FUEL", 1])
    print(leftOvers)
    return result["ORE"]


def part2(data):
    return "not implemented"
