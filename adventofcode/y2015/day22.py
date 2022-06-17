import copy
import sys


class Fighter:
    def __init__(self, name, hp, damage, mana=0, hpDecay=0, debug=False) -> None:
        self.name = name
        self.hp = hp
        self.damage = damage

        self.armor = 0
        self.mana = mana

        self.shieldTimer = -1
        self.poisonTimer = -1
        self.rechargeTimer = -1

        self.hpDecay = hpDecay

        self.debug = debug

    def __str__(self) -> str:
        result = "- {} has {} hit points".format(self.name, self.hp)
        if self.name == "Player":
            result += ", {} armor, {} mana".format(self.armor, self.mana)
        return result

    def startTurn(self, decay=False):
        if decay and self.hpDecay > 0:
            self.hp -= self.hpDecay
            if self.debug:
                print("Player hp decays by 1")
            if self.hp <= 0:
                return False

        self.shieldTimer = max(-1, self.shieldTimer - 1)
        self.poisonTimer = max(-1, self.poisonTimer - 1)
        self.rechargeTimer = max(-1, self.rechargeTimer - 1)

        if self.shieldTimer >= 0:
            if self.debug:
                print("Shield's timer is now {}.".format(self.shieldTimer))
            self.armor = 7
        else:
            self.armor = 0

        if self.poisonTimer >= 0:
            if self.debug:
                print(
                    "Poison deals 3 damage; its timer is now {}.".format(
                        self.poisonTimer
                    )
                )
            self.hp -= 3

        if self.rechargeTimer >= 0:
            if self.debug:
                print(
                    "Recharge provides 101 mana; its timer is now {}.".format(
                        self.rechargeTimer
                    )
                )
            self.mana += 101

        if self.debug and self.shieldTimer == 0:
            print("Shield wears off.")

        if self.debug and self.poisonTimer == 0:
            print("Poison wears off.")

        if self.debug and self.rechargeTimer == 0:
            print("Recharge wears off.")

        return self.hp > 0

    def dealDamage(self, other, damage=None):
        if damage == None:
            other.takeDamage(self.damage)
        else:
            other.takeDamage(damage)

    def takeDamage(self, amount):
        self.hp -= max(1, amount - self.armor)

    def addShield(self):
        self.shieldTimer = 6

    def addPoison(self):
        self.poisonTimer = 6

    def addRecharge(self):
        self.rechargeTimer = 5


def findBest(player, boss, manaUsage=0, spellUsed=[], bestFound=sys.maxsize):

    if player.hp <= 0 or manaUsage > bestFound:
        return False, manaUsage, spellUsed
    if boss.hp <= 0:
        return True, manaUsage, spellUsed

    spells = [
        ("Magic Missile", 53),
        ("Drain", 73),
        ("Shield", 113),
        ("Poison", 173),
        ("Recharge", 229),
    ]

    best = bestFound
    bestCast = []

    for spellNum in range(len(spells)):
        spell = spells[spellNum]
        cast = spellUsed.copy()
        cast.append(spell[0])
        manaUsed = manaUsage + spell[1]
        newPlayer = copy.deepcopy(player)
        newBoss = copy.deepcopy(boss)

        if not newPlayer.startTurn(True):
            return False, sys.maxsize, cast
        if not newBoss.startTurn():
            return True, manaUsed, cast

        if newPlayer.mana < spell[1]:
            continue

        if spellNum == 2 and newPlayer.shieldTimer > 0:
            continue
        if spellNum == 3 and newBoss.poisonTimer > 0:
            continue
        if spellNum == 4 and newPlayer.rechargeTimer > 0:
            continue

        newPlayer.mana -= spell[1]

        if spellNum == 0:
            newPlayer.dealDamage(newBoss, 4)
        elif spellNum == 1:
            newPlayer.dealDamage(newBoss, 2)
            newPlayer.hp += 2
        elif spellNum == 2:
            newPlayer.addShield()
        elif spellNum == 3:
            newBoss.addPoison()
        elif spellNum == 4:
            newPlayer.addRecharge()

        if newBoss.hp <= 0:
            return True, manaUsed, cast

        if not newPlayer.startTurn():
            return False, sys.maxsize, cast
        if not newBoss.startTurn():
            return True, manaUsed, cast

        newBoss.dealDamage(newPlayer)

        check = findBest(newPlayer, newBoss, manaUsed, cast, best)
        if check[0] and check[1] < best:
            best = check[1]
            bestCast = check[2]

    return best, best, bestCast


def fightFighters(player, boss, useSpells=[]):
    manaUsed = 0

    spells = [
        ("Magic Missile", 53),
        ("Drain", 73),
        ("Shield", 113),
        ("Poison", 173),
        ("Recharge", 229),
    ]

    turn = 0

    while player.hp > 0 and boss.hp > 0:
        print("\n-- Round {} --".format(turn + 1))
        print("\n-- Player turn --")
        print(player)
        print(boss)
        if not player.startTurn(True):
            return False, manaUsed
        if not boss.startTurn():
            return True, manaUsed

        if len(useSpells) != 0:
            if turn >= len(useSpells):
                return False, manaUsed
            castSpell = useSpells[turn]
            turn += 1
        else:
            while True:
                castSpell = int(input("Spell num (0-4):"))
                if castSpell == 2 and player.shieldTimer > 0:
                    continue
                if castSpell == 3 and boss.poisonTimer > 0:
                    continue
                if castSpell == 4 and player.rechargeTimer > 0:
                    continue
                break

        if player.mana < spells[castSpell][1]:
            return False, manaUsed

        player.mana -= spells[castSpell][1]

        if castSpell == 0:
            print("Player casts {}, dealing 4 damage.".format(spells[castSpell][0]))
            player.dealDamage(boss, 4)
        elif castSpell == 1:
            print(
                "Player casts {}, dealing 2 damage, and healing 2 hit points.".format(
                    spells[castSpell][0]
                )
            )
            player.dealDamage(boss, 2)
            player.hp += 2
        elif castSpell == 2:
            print("Player casts {}.".format(spells[castSpell][0]))
            player.addShield()
        elif castSpell == 3:
            print("Player casts {}.".format(spells[castSpell][0]))
            boss.addPoison()
        elif castSpell == 4:
            print("Player casts {}.".format(spells[castSpell][0]))
            player.addRecharge()

            manaUsed += spells[castSpell][1]

        if boss.hp <= 0:
            return True, manaUsed

        print("\n-- Boss turn --")
        print(player)
        print(boss)
        if not player.startTurn():
            return False
        if not boss.startTurn():
            return True, manaUsed

        print("Boss attacks for {} damage.".format(boss.damage))
        boss.dealDamage(player)

        input()
    return False, manaUsed


def getBoss(data, debug=False):
    bossHP = int(data.pop(0).split(": ")[1])
    bossDamage = int(data.pop(0).split(": ")[1])
    return Fighter("Boss", bossHP, bossDamage, debug=debug)


def part1(data, test=False) -> str:
    boss = getBoss(data)
    player = Fighter("Player", 50, 0, 500)
    return str(findBest(player, boss)[1])


def part2(data, test=False) -> str:
    boss = getBoss(data)
    player = Fighter("Player", 50, 0, 500, 1)

    # if fightFighters(player, boss, [3, 1, 4, 3, 2, 4, 3, 1, 0]):
    #    print("win")
    # return
    return str(findBest(player, boss, 0, [], sys.maxsize)[1])
