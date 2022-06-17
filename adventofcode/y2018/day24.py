from math import floor
import re
from tkinter import ALL


class Unit:
    def __init__(self, armyNum, unitNum, inData) -> None:

        self.armyNum = armyNum
        self.unitNum = unitNum
        self.isAlive = True

        reStr = "([0-9]+) units each with ([0-9]+) hit points (?:\((.+)\) |)with an attack that does ([0-9]+) (.+) damage at initiative ([0-9]+)"
        reResult = re.search(reStr, inData)

        self.maxUnits = int(reResult.group(1))
        self.unitCount = int(reResult.group(1))
        self.hitPoints = int(reResult.group(2))
        self.originalDamage = int(reResult.group(4))
        self.damage = int(reResult.group(4))
        self.damageType = reResult.group(5)
        self.initiative = int(reResult.group(6))
        self.weaknesses = []
        self.immunities = []

        if reResult.group(3) != None:
            group3Split = reResult.group(3).split("; ")
            if group3Split[0][0] == "w":
                self.weaknesses = group3Split[0][8:].split(", ")
            else:
                self.immunities = group3Split[0][10:].split(", ")
            if len(group3Split) == 2:
                if group3Split[1][0] == "w":
                    self.weaknesses = group3Split[1][8:].split(", ")
                else:
                    self.immunities = group3Split[1][10:].split(", ")

        self.target = None
        self.isTarget = False

    def __str__(self) -> str:
        if self.armyNum == 0:
            return "Immune System Group " + str(self.unitNum)
        else:
            return "Infection Group " + str(self.unitNum)

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Unit):
            return False
        return self.armyNum == __o.armyNum and self.unitNum == __o.unitNum

    def __lt__(self, __o: "Unit") -> bool:
        if self.getEffectivePower() == __o.getEffectivePower():
            return self.initiative < __o.initiative
        return self.getEffectivePower() < __o.getEffectivePower()

    def getEffectivePower(self):
        return self.unitCount * self.damage

    def checkDamageTo(self, otherUnit: "Unit"):
        multiplier = 1
        if self.damageType in otherUnit.weaknesses:
            multiplier = 2
        elif self.damageType in otherUnit.immunities:
            multiplier = 0
        return self.getEffectivePower() * multiplier

    def dealDamage(self):
        killCount = 0
        if self.isAlive and self.target != None:
            damageAmount = self.checkDamageTo(self.target)
            beforeUnitCount = self.target.unitCount
            self.target.takeDamage(damageAmount)
            killCount = beforeUnitCount - self.target.unitCount
            self.target.isTarget = False
            self.target = None
        return killCount

    def takeDamage(self, damageAmount):
        unitsLost = floor(damageAmount / self.hitPoints)
        self.unitCount -= unitsLost
        if self.unitCount <= 0:
            self.isAlive = False
            if self.target != None:
                self.target.isTarget = False
            self.unitCount = 0

    def chooseTarget(self, otherArmy):
        if not self.isAlive:
            return
        bestDamage = 0
        targets = []
        for otherUnit in otherArmy:
            if otherUnit.isAlive and not otherUnit.isTarget:
                checkDamage = self.checkDamageTo(otherUnit)
                if checkDamage > bestDamage:
                    targets = []
                    bestDamage = checkDamage
                if checkDamage == bestDamage:
                    targets.append(otherUnit)
        if len(targets) > 0:
            targets.sort()
            targets = targets[::-1]
            self.target = targets[0]
            self.target.isTarget = True

    def boostUnit(self, boostAmount):
        self.damage += boostAmount

    def resetUnit(self):
        self.target = None
        self.isAlive = True
        self.isTarget = False
        self.unitCount = self.maxUnits
        self.damage = self.originalDamage


def parseInput(data):
    armies = [[], []]
    armyIndex = 0
    data.pop(0)
    line = data.pop(0)
    unitNum = 1
    while line != None:
        if line == "":
            armyIndex += 1
            unitNum = 1
            data.pop(0)
        else:
            armies[armyIndex].append(Unit(armyIndex, unitNum, line))
            unitNum += 1
        if len(data) == 0:
            break
        line = data.pop(0)
    return armies


def doBattle(army1, army2, boost=0):
    allUnits = []
    allUnits.extend(army1)
    allUnits.extend(army2)
    allUnits.sort(key=lambda x: x.initiative, reverse=True)

    for unit in allUnits:
        unit.resetUnit()

    for unit in army1:
        unit.boostUnit(boost)
    round = 1

    while checkArmy(army1) and checkArmy(army2):
        army1.sort(reverse=True)
        army2.sort(reverse=True)
        round += 1

        for unit in army2:
            unit.chooseTarget(army1)

        for unit in army1:
            unit.chooseTarget(army2)

        totalKills = 0
        for unit in allUnits:
            if unit.isAlive:
                totalKills += unit.dealDamage()
        if totalKills == 0:
            return [army1, army2]

    return [army1, army2]


def checkArmy(army):
    for unit in army:
        if unit.isAlive:
            return True
    return False


def part1(data, test=False) -> str:
    armies = parseInput(data)
    armies = doBattle(armies[0], armies[1])

    result = 0
    for unit in armies[1]:
        result += unit.unitCount

    return result


def part2(data, test=False) -> str:
    armies = parseInput(data)
    boostAmount = 30
    while True:
        armies = doBattle(armies[0], armies[1], boostAmount)

        if not checkArmy(armies[1]) and checkArmy(armies[0]):
            break
        boostAmount += 1

    result = 0
    for unit in armies[0]:
        result += unit.unitCount

    return result  # Not sure why it is 24 off.... :/
