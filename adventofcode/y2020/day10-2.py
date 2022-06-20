from typing import List
from functools import lru_cache

ADAPTERS: List[int] = []


@lru_cache(maxsize=None)
def check_adapters(pointer):

    if pointer == len(ADAPTERS) - 1:
        return 1

    count = 0
    if pointer + 1 < len(ADAPTERS) and ADAPTERS[pointer + 1] - ADAPTERS[pointer] <= 3:
        count += check_adapters(pointer + 1)

    if pointer + 2 < len(ADAPTERS) and ADAPTERS[pointer + 2] - ADAPTERS[pointer] <= 3:
        count += check_adapters(pointer + 2)

    if pointer + 3 < len(ADAPTERS) and ADAPTERS[pointer + 3] - ADAPTERS[pointer] <= 3:
        count += check_adapters(pointer + 3)

    return count


inFile = open("day10.in", "r").read().split("\n")
inFile.pop()

intFile = [int(x) for x in inFile]
ADAPTERS = [0] + sorted(intFile) + [max(intFile) + 3]

result = check_adapters(0)

print(result)
