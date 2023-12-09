import math
from dataclasses import dataclass

@dataclass
class Point:
    x : int
    y : int
    dist : float = 0.0
    eliv : str = ''

    def distance_between(self, other):
        horiz = math.pow(self.x - other.x, 2)
        vert = math.pow(self.y - other.y, 2)
        self.dist = math.sqrt(horiz + vert)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return hash(self.x) + hash(self.y)