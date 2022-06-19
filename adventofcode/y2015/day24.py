from math import prod
from typing import List, Any


class Sleigh:
    def __init__(self, packages=[], useTrunk=False) -> None:
        self.allPackages = packages
        self.allPackages.sort(reverse=True)

        if useTrunk:
            self.compartmentTotal = sum(self.allPackages) / 4
        else:
            self.compartmentTotal = sum(self.allPackages) / 3

        self.options: List[List[Any]] = []
        self.best: List[Any] = []

        self.useTrunk = useTrunk

    def distributePackages(self):
        startI = 0
        while startI < len(self.allPackages):
            packages = self.allPackages.copy()
            group1 = []
            group2 = []
            group3 = []
            i = startI
            while i < len(self.allPackages):
                group1Sum = sum(group1)
                group2Sum = sum(group2)
                group3Sum = sum(group3)
                if not self.allPackages[i] in packages:
                    pass
                elif group1Sum + self.allPackages[i] <= self.compartmentTotal:
                    group1.append(self.allPackages[i])
                    packages.remove(self.allPackages[i])
                    if group1Sum + self.allPackages[i] == self.compartmentTotal:
                        i = 0
                elif group2Sum + self.allPackages[i] <= self.compartmentTotal:
                    group2.append(self.allPackages[i])
                    packages.remove(self.allPackages[i])
                    if group2Sum + self.allPackages[i] == self.compartmentTotal:
                        i = 0
                elif (
                    self.useTrunk
                    and group3Sum + self.allPackages[i] <= self.compartmentTotal
                ):
                    group3.append(self.allPackages[i])
                    packages.remove(self.allPackages[i])
                i += 1

            if sum(packages) == self.compartmentTotal:
                if len(self.options) == 0 or len(group1) < len(self.options[0][0]):
                    self.options = [
                        [group1.copy(), group2.copy(), group3.copy(), packages.copy()]
                    ]
                    self.best = [
                        group1.copy(),
                        group2.copy(),
                        group3.copy(),
                        packages.copy(),
                    ]
                elif len(group1) == len(self.options[0][0]):
                    self.options.append(
                        [group1.copy(), group2.copy(), group3.copy(), packages.copy()]
                    )
                    if prod(group1) < prod(self.best[0]):
                        self.best = [
                            group1.copy(),
                            group2.copy(),
                            group3.copy(),
                            packages.copy(),
                        ]

            startI += 1


def fillContainer(packages, target, container=[], bestContainer=[]):
    containerSum = sum(container)
    best = bestContainer
    bestProd = None

    if containerSum >= target:
        return containerSum == target, sorted(container, reverse=True)

    if len(best) > 0 and len(container) >= len(best):
        return False, None

    for i in range(len(packages)):
        newPackages = packages.copy()
        newContainer = container.copy()
        newPackages.remove(packages[i])
        newContainer.append(packages[i])

        check = fillContainer(
            newPackages.copy(), target, newContainer.copy(), best.copy()
        )

        if check[0]:
            if len(best) == 0 or len(check[1]) < len(best):
                best = check[1]
            elif len(check[1]) == len(best) and (
                bestProd == None or prod(check[1]) <= bestProd
            ):
                bestProd = prod(check[1])
                best = check[1]
    return True, best


def part1(data, test=False) -> str:
    packages = [int(x) for x in data]
    sleigh = Sleigh(packages)
    sleigh.distributePackages()
    return str(prod(sleigh.best[0]))


def part2(data, test=False) -> str:
    packages = [int(x) for x in data]
    packages.sort(reverse=True)
    groups = fillContainer(packages, sum(packages) / 4, [])[1]
    return str(prod(groups))
