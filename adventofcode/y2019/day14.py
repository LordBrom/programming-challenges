import sys
import re
import math
import random


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
        fore = self.dictionary[product[0]].produceAmount(
            self.dictionary, product[1])
        back = self.dictionary[product[0]].produceAmount(
            self.dictionary, product[1], {}, "", -1)

        if fore[0]['ORE'] < back[0]['ORE']:
            return fore
        else:
            return back


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

    def produceAmount(self, dictionary, amount, inventory={}, space="", sortVal=1):
        timesProduced = math.ceil(amount / self.output[0])
        self.debugPrint([space, "producing", amount,
                        self.output[1], "from inventory", inventory])

        requirements = {}
        newRequirements = {}

        self.input = sorted(self.input, key=lambda x: sortVal*x[0])

        for i in self.input:
            if i[1] == "ORE":
                newRequirements["ORE"] = i[0] * timesProduced
            else:
                self.debugPrint([space, "needs", i[0] * timesProduced, i[1]])
                inputNeeded = i[0] * timesProduced

                if i[1] in inventory and inventory[i[1]] != 0:
                    leftOversUsed = min(inputNeeded, inventory[i[1]])
                    inputNeeded -= leftOversUsed
                    inventory[i[1]] -= leftOversUsed
                    self.debugPrint([space, "Using", leftOversUsed, "from inventory",
                                    inventory[i[1]], "leftovers remain"])

                if inputNeeded != 0:
                    forward = dictionary[i[1]].produceAmount(
                        dictionary, inputNeeded, inventory.copy(), space + "    ",)
                    backward = dictionary[i[1]].produceAmount(
                        dictionary, inputNeeded, inventory.copy(), space + "    ", -1)
                    newRequirements = forward[0]
                    inventory = forward[1]

                    if "ORE" in forward[0] and "ORE" in backward[0]:
                        if forward[0]['ORE'] < backward[0]['ORE']:
                            newRequirements = forward[0]
                            inventory = forward[1]
                        else:
                            newRequirements = backward[0]
                            inventory = backward[1]
                    else:

                        if "ORE" in forward[0]:
                            newRequirements = forward[0]
                            inventory = forward[1]
                        else:
                            newRequirements = backward[0]
                            inventory = backward[1]

            for r in newRequirements:
                if not r in requirements:
                    requirements[r] = 0
                requirements[r] += newRequirements[r]

        if not self.output[1] in inventory:
            inventory[self.output[1]] = 0
        remainder = (self.output[0] * timesProduced) - amount
        inventory[self.output[1]] += remainder

        self.debugPrint([space, self.output[1], "created using", requirements, "with",
                        remainder, "left over", inventory])

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
    recipeDictionary = RecipeDictionary(data)
    return recipeDictionary.produceOutput(["FUEL", 1])[0]["ORE"]


def part2(data):
    recipeDictionary = RecipeDictionary(data)
    best = sys.maxsize

    cargoSize = 1000000000000

    #num = math.floor(cargoSize / part1(data))
    num = 6972985
    result = 0
    while result <= cargoSize:
        num += 1
        result = recipeDictionary.produceOutput(["FUEL", num])[0]["ORE"]
        if result < best:
            best = result
    return num - 1
