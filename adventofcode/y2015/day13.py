import re

RE_STR = "(.+) would (gain|lose) ([0-9]+) happiness units by sitting next to (.+)."


def findSeatOrder(people, person, seated=[], happiness=0):
    best = happiness
    seated.append(person)
    bestSteated = seated

    if len(seated) == len(people):
        return best + getHappiness(people, seated[0], seated[-1]), bestSteated

    for next in people[person]:
        if not next in seated:
            check, checkSeated = findSeatOrder(people, next, seated.copy(
            ), happiness + getHappiness(people, person, next))
            if check > best:
                best = check
                bestSteated = checkSeated

    return best, bestSteated


def getHappiness(people, person1, person2):
    return people[person1][person2] + people[person2][person1]


def parseInput(data):
    people = {}

    for d in data:
        reResult = re.search(RE_STR, d)
        if not reResult.group(1) in people:
            people[reResult.group(1)] = {}
        if reResult.group(2) == "gain":
            people[reResult.group(1)][reResult.group(4)
                                      ] = int(reResult.group(3))
        else:
            people[reResult.group(1)][reResult.group(4)
                                      ] = -int(reResult.group(3))
    return people


def part1(data):
    people = parseInput(data)
    happiness, order = findSeatOrder(people, 'Alice', [], 0)
    return happiness


def part2(data):
    people = parseInput(data)
    people['You'] = {}
    for person in people:
        people[person]['You'] = 0
        people['You'][person] = 0
    happiness, order = findSeatOrder(people, 'Alice', [], 0)
    return happiness
