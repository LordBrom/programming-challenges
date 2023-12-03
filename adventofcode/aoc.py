def manhattan_distance(point1: tuple, point2: tuple) -> float:
    if len(point1) != len(point2):
        raise Exception("The 2 points require the same number of coords")
    result = 0
    for i in range(len(point1)):
        result += abs(point1[i] - point2[i])
    return result


def get_neighbors(grid, x, y, diagonal = False):
    adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    if diagonal:
        adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1,-1), (0, -1)]
    neighbors = []
    for dx, dy in adjacent:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            neighbors.append((nx, ny))
    return neighbors

class Point:
    def __init__(self, x: int, y: int, z: int = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"{self.x}, {self.y}, {self.z}"

    def __eq__(self, __o: object) -> bool:
        return (
            isinstance(__o, Point)
            and self.x == __o.x
            and self.y == __o.y
            and self.z == __o.z
        )

    def __hash__(self):
        return hash((self.x, self.y, self.z))
        # return hash(self.x * 10000 + self.y * 100 + self.z)

    def as_tuple(self) -> tuple:
        return (self.x, self.y, self.z)

    def add_point(self, other: "Point") -> None:
        self.x += other.x
        self.y += other.y
        self.z += other.z
