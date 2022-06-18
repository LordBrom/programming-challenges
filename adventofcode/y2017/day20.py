import re
from sys import maxsize
from typing import List, Match
from aoc import Point, manhattan_distance


class Particle:
    def __init__(
        self, num: int, position: Point, velocity: Point, acceleration: Point
    ) -> None:
        self.num = num
        self.pos = position
        self.vel = velocity
        self.acc = acceleration
        self.distFromCenter = maxsize

    def __str__(self) -> str:
        return f"{self.num}: p=<{self.pos}>, v=<{self.vel}>, a=<{self.acc}>, d={self.distFromCenter}"

    def time_tick(self) -> None:
        self.vel.add_point(self.acc)
        self.pos.add_point(self.vel)
        newDistFromCenter = int(manhattan_distance(self.pos.as_tuple(), (0, 0, 0)))
        self.distFromCenter = newDistFromCenter


def parse_input(data) -> List[Particle]:
    result: List[Particle] = []
    for i, d in enumerate(data):
        reStr = "p=<([-0-9]+),([-0-9]+),([-0-9]+)>, v=<([-0-9]+),([-0-9]+),([-0-9]+)>, a=<([-0-9]+),([-0-9]+),([-0-9]+)>"
        reResult: Match[str] = re.search(reStr, d)
        particlePosition = Point(
            int(reResult.group(1)), int(reResult.group(2)), int(reResult.group(3))
        )
        particleVelocity = Point(
            int(reResult.group(4)), int(reResult.group(5)), int(reResult.group(6))
        )
        particleAcceleration = Point(
            int(reResult.group(7)), int(reResult.group(8)), int(reResult.group(9))
        )
        result.append(
            Particle(i, particlePosition, particleVelocity, particleAcceleration)
        )
    return result


def part1(data, test=False) -> str:
    particles = parse_input(data)
    for i in range(500):
        for particle in particles:
            particle.time_tick()

    particles.sort(key=lambda x: x.distFromCenter)

    return str(particles[0].num)


def part2(data, test=False) -> str:
    particles = parse_input(data)

    for i in range(500):
        if len(particles) == 1:
            break
        for particle in particles:
            particle.time_tick()

        x = 0
        while x < len(particles):
            collide = False
            y = 0
            while y < len(particles):
                if x != y:
                    if particles[x].pos == particles[y].pos:
                        collide = True
                        particles.remove(particles[y])
                        y -= 1
                y += 1
            if collide:
                particles.remove(particles[x])
            else:
                x += 1

    return str(len(particles))
