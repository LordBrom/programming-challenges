import math
from typing import Dict, List, Any, Optional


def findAsteroids(data):
    result = []

    for row in enumerate(data):
        for col in enumerate(row[1]):
            if data[row[0]][col[0]] == "#":
                result.append([row[0], col[0]])

    return result


def calc_angle(p1, p2):
    deltaX = p1[0] - p2[0]
    deltaY = p1[1] - p2[1]
    angle = math.atan2(deltaX, deltaY) / math.pi

    angle = angle - 0.5

    if angle >= 0:
        return angle
    else:
        return 2 + angle


def count_visible(asteroids, current):
    foundAngles = []
    for asteroid in asteroids:
        if asteroid == current:
            continue
        angle = calc_angle(current, asteroid)
        if not angle in foundAngles:
            foundAngles.append(angle)
    return foundAngles


def calc_dist(p1, p2):
    deltaX = p1[0] - p2[0]
    deltaY = p1[1] - p2[1]

    dist = math.sqrt((deltaX) ** 2 + (deltaY) ** 2)

    return dist


def part1(data, test=False) -> str:

    asteroids = findAsteroids(data)

    result = 0
    for asteroid in asteroids:
        result = max(result, len(count_visible(asteroids, asteroid)))

    return str(result)


def part2(data, test=False) -> str:

    asteroids = findAsteroids(data)

    check = 0
    bestAsteroid = None
    for asteroid in asteroids:
        newCheck = len(count_visible(asteroids, asteroid))
        if newCheck > check:
            check = newCheck
            bestAsteroid = asteroid

    angles = []
    asteroidAngles: Dict[Any, Any] = {}

    for asteroid in asteroids:
        if asteroid == bestAsteroid:
            continue
        angle = calc_angle(bestAsteroid, asteroid)
        if not angle in angles:
            angles.append(angle)
            asteroidAngles[angle] = []
        asteroidAngles[angle].append([asteroid, calc_dist(bestAsteroid, asteroid)])

    angles.sort()
    for asteroidAngle in asteroidAngles:
        asteroids = asteroidAngles[asteroidAngle]
        asteroidAngles[asteroidAngle] = sorted(asteroids, key=lambda x: x[1])

    findCount = 200
    result: Optional[List[List[int]]] = None

    count = 0
    pointer = 0
    while True:
        count += 1
        curAngle = angles[pointer]
        asteroid = asteroidAngles[curAngle].pop(0)
        if count == findCount:
            result = asteroid[0]
        if len(asteroidAngles[curAngle]) == 0:
            angles.pop(pointer)
            if len(angles) == 0:
                break
            pointer = pointer % len(angles)
        else:
            pointer += 1
            pointer = pointer % len(angles)

    return str((result[1] * 100) + result[0])
