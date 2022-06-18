import re


class SolarSystem:
    def __init__(self, startPositions):
        self.planets = []
        for position in startPositions:
            self.planets.append(Planet(position))

    def takeStep(self):
        self.setVelocities()
        for p in self.planets:
            p.move()

    def setVelocities(self):
        for p1 in range(len(self.planets)):
            gravity = [0, 0, 0]
            for p2 in range(len(self.planets)):
                if p1 == p2:
                    continue
                for i in range(3):
                    if self.planets[p1].position[i] < self.planets[p2].position[i]:
                        gravity[i] += 1
                    elif self.planets[p1].position[i] > self.planets[p2].position[i]:
                        gravity[i] -= 1
            self.planets[p1].updateVelocity(gravity)

    def getSystemEnergy(self):
        result = 0
        for p in self.planets:
            result += p.potentialEnergy() * p.kineticEnergy()
        return result

    def getPlanetPositions(self):
        planetPositions = []
        for p in self.planets:
            planetPositions.append(p.position.copy())
            planetPositions.append(p.velocity.copy())
        return planetPositions


class Planet:
    def __init__(self, dataStr):
        reStr = "<x=([-0-9]+), y=([-0-9]+), z=([-0-9]+)>"
        reResult = re.search(reStr, dataStr)
        self.position = [
            int(reResult.group(1)),
            int(reResult.group(2)),
            int(reResult.group(3)),
        ]
        self.velocity = [0, 0, 0]

    def updateVelocity(self, gravity):
        self.velocity[0] += gravity[0]
        self.velocity[1] += gravity[1]
        self.velocity[2] += gravity[2]

    def move(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def potentialEnergy(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def kineticEnergy(self):
        return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])


def part1(data, test=False) -> str:
    system = SolarSystem(data)

    for step in range(1000):
        system.takeStep()

    return str(system.getSystemEnergy())


def part2(data, test=False) -> str:
    system = SolarSystem(data)

    positions = []
    step = 0
    while True:
        planetPositions = system.getPlanetPositions()
        if planetPositions in positions:
            break
        positions.append(planetPositions)
        system.takeStep()
        step += 1

    return str(step)
