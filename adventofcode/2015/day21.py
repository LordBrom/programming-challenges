import numpy as np


class Equipment():
    def __init__(self, cost, damage, armor, name) -> None:
        self.cost = cost
        self.damage = damage
        self.armor = armor
        self.name = name
        pass


class Fighter():
    def __init__(self, name, hp=100, damage=0, armor=0) -> None:
        self.name = name
        self.hp = hp
        self.hpOg = hp
        self.damage = damage
        self.armor = armor
        self.equipCost = 0
        self.equipment = []

    def __str__(self) -> str:
        result = "hp: {}; damage: {}; armor: {}".format(
            self.hp, self.damage, self.armor)
        if len(self.equipment):
            result += "\nequipment"
            for equip in self.equipment:
                result += "\n     {} ({})".format(equip.name, equip.cost)
        return result

    def reset(self):
        self.hp = self.hpOg
        self.equipCost = 0
        self.equipment = []

    def takeDamage(self, amount):
        self.hp -= max(1, amount - self.armor)

    def fight(self, other: 'Fighter'):
        other.takeDamage(self.damage)
        # print("The {} deals {}-{} = {} damage; the {} goes down to {} hit points.".format(
        #    self.name, self.damage, other.armor, max(1, self.damage - other.armor), other.name, other.hp))

    def equipItem(self, item: 'Equipment'):
        self.equipCost += item.cost
        self.damage += item.damage
        self.armor += item.armor
        self.equipment.append(item)


def fightFighters(player: Fighter, boss: Fighter):
    while player.hp > 0 and boss.hp > 0:
        player.fight(boss)
        if boss.hp <= 0:
            return True
        boss.fight(player)
    return False


def setupEquipment():
    equipment = {}
    equipment['weapons'] = []
    equipment['armor'] = []
    equipment['rings'] = []

    equipment['weapons'].append(Equipment(8, 4, 0, "Dagger"))
    equipment['weapons'].append(Equipment(10, 5, 0, "Shortsword"))
    equipment['weapons'].append(Equipment(25, 6, 0, "warhammer"))
    equipment['weapons'].append(Equipment(40, 7, 0, "Longsword"))
    equipment['weapons'].append(Equipment(74, 8, 0, "Greataxe"))

    equipment['armor'].append(Equipment(13, 0, 1, "Leather"))
    equipment['armor'].append(Equipment(31, 0, 2, "Chainmail"))
    equipment['armor'].append(Equipment(53, 0, 3, "Splintmail"))
    equipment['armor'].append(Equipment(75, 0, 4, "Bandedmail"))
    equipment['armor'].append(Equipment(102, 0, 5, "Platemail"))

    equipment['rings'].append(Equipment(25, 1, 0, "Damage +1"))
    equipment['rings'].append(Equipment(50, 2, 0, "Damage +2"))
    equipment['rings'].append(Equipment(100, 3, 0, "Damage +3"))
    equipment['rings'].append(Equipment(20, 0, 1, "Defense +1"))
    equipment['rings'].append(Equipment(40, 0, 2, "Defense +2"))
    equipment['rings'].append(Equipment(80, 0, 3, "Defense +3"))

    return equipment


def part1(data):
    bossHP = int(data.pop(0).split(": ")[1])
    bossDamage = int(data.pop(0).split(": ")[1])
    bossArmor = int(data.pop(0).split(": ")[1])

    equipment = setupEquipment()

    winningCombos = []

    for damage in range(4, 12):
        for armor in range(0, 12):
            bossFighter = Fighter("Boss", bossHP, bossDamage, bossArmor)
            playerFighter = Fighter("Player", 100, damage, armor)
            if fightFighters(playerFighter, bossFighter):
                winningCombos.append([damage, armor])
                break

    bossFighter = Fighter("Boss", bossHP, bossDamage, bossArmor)
    playerFighter = Fighter("Player")

    playerFighter.equipItem(equipment['weapons'][3])
    playerFighter.equipItem(equipment['rings'][1])
    playerFighter.equipItem(equipment['armor'][1])

    fightFighters(playerFighter, bossFighter)
    return playerFighter.equipCost


def part2(data):
    bossHP = int(data.pop(0).split(": ")[1])
    bossDamage = int(data.pop(0).split(": ")[1])
    bossArmor = int(data.pop(0).split(": ")[1])

    equipment = setupEquipment()

    winningCombos = []

    for damage in reversed(range(4, 14)):
        for armor in reversed(range(0, 12)):
            bossFighter = Fighter("Boss", bossHP, bossDamage, bossArmor)
            playerFighter = Fighter("Player", 100, damage, armor)
            if not fightFighters(playerFighter, bossFighter):
                winningCombos.append([damage, armor])
                break

    bossFighter = Fighter("Boss", bossHP, bossDamage, bossArmor)
    playerFighter = Fighter("Player")

    playerFighter.equipItem(equipment['weapons'][0])
    playerFighter.equipItem(equipment['rings'][2])
    playerFighter.equipItem(equipment['armor'][0])
    playerFighter.equipItem(equipment['rings'][5])

    fightFighters(playerFighter, bossFighter)

    return playerFighter.equipCost

# 186 - low

# to try:
