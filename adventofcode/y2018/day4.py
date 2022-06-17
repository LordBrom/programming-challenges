import re

RGDATE = 1
RGHOUR = 2
RGMIN = 3
RGMSG = 4
RESTR = "\[([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}):([0-9]{2})\] ([a-zA-Z0-9# ]+)"
REMSG = "Guard #([0-9]+) begins shift"


class GuardSleepTrack:
    def __init__(self, guardID):
        self.guardID = guardID
        self.days = {}

    def add_date(self, date):
        if (date in self.days):
            return
        #print(date + " added to guard " + self.guardID + "'s sched")
        self.days[date] = [False for x in range(60)]

    def add_sleep(self, date, start, end):
        self.add_date(date)
        for i in range(start, end):
            self.days[date][i] = True

    def count_sleep(self):
        result = 0
        for d in self.days:
            for t in self.days[d]:
                if t:
                    result += 1
        return result

    def find_sleepiest_hour(self, returnHour=True):
        result = -1
        bestT = -1
        for t in range(60):
            best = 0
            for d in self.days:
                if self.days[d][t]:
                    best += 1
            if bestT < best:
                result = t
                bestT = best

        if returnHour:
            return result
        else:
            return bestT

    def print_sched(self):
        print("")
        print("guard " + self.guardID + "'s schedule")
        dateStr = "            "
        for d in range(60):
            if len(str(d)) == 1:
                dateStr += " "
            dateStr += " " + str(d)
        print(dateStr)
        for d in self.days:
            rowStr = str(d) + "  "
            for s in self.days[d]:
                if s:
                    rowStr += '  #'
                else:
                    rowStr += '  .'
            print(rowStr)

        print("")
        print("")


def buildSchedules(input):
    result = {}
    currentGuardId = 0
    isSleeping = False
    sleepStart = 0

    for i in input:
        reResult = re.search(RESTR, i)

        if reResult.group(RGMSG)[0] == 'G':
            if currentGuardId != 0 and isSleeping:
                result[currentGuardId].add_sleep(
                    reResult.group(RGDATE),
                    sleepStart,
                    getTime(
                        reResult.group(RGHOUR),
                        reResult.group(RGMIN)
                    )
                )

            currentGuardId = re.search(REMSG, reResult.group(RGMSG)).group(1)
            if not currentGuardId in result:
                result[currentGuardId] = GuardSleepTrack(currentGuardId)

        elif reResult.group(RGMSG)[0] == 'f':
            isSleeping = True
            sleepStart = getTime(reResult.group(RGHOUR), reResult.group(RGMIN))

        elif reResult.group(RGMSG)[0] == 'w':
            isSleeping = False
            result[currentGuardId].add_sleep(
                reResult.group(RGDATE),
                sleepStart,
                getTime(
                    reResult.group(RGHOUR),
                    reResult.group(RGMIN)
                )
            )
    return result


def getTime(h, m):
    return (int(h) * 60) + int(m)


def part1(input):
    guardTracks = buildSchedules(input)

    sleepiestGuard = 0
    guardSleep = 0
    for g in guardTracks:
        newGuardSleep = guardTracks[g].count_sleep()
        if newGuardSleep > guardSleep:
            guardSleep = newGuardSleep
            sleepiestGuard = g

    sleepiestHour = guardTracks[sleepiestGuard].find_sleepiest_hour()

    return int(sleepiestGuard) * int(sleepiestHour)


def part2(input):
    guardTracks = buildSchedules(input)

    sleepiestGuard = 0
    guardSleep = 0
    for g in guardTracks:
        newGuardSleep = guardTracks[g].find_sleepiest_hour(False)
        if newGuardSleep > guardSleep:
            guardSleep = newGuardSleep
            sleepiestGuard = g

    sleepiestHour = guardTracks[sleepiestGuard].find_sleepiest_hour()

    return int(sleepiestGuard) * int(sleepiestHour)
