class Point:
    x = 0
    y = 0

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) + hash(self.y)

    def __repr__(self):
        return '<Point ({},{})>'.format(self.x, self.y)

    def touching(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def diagonal(self, other):
        return abs(self.x - other.x) >= 1 and abs(self.y - other.y) >= 1

    def up(self):
        return Point(self.x, self.y + 1)

    def down(self):
        return Point(self.x, self.y - 1)

    def right(self):
        return Point(self.x + 1, self.y)

    def left(self):
        return Point(self.x - 1, self.y)


class Knot:
   name = ""
   point = None
   visited = None

   def __init__(self, name="fart", point = Point(0, 0)):
       self.name = name
       self.point = point
       self.visited = set()
       self.visited.add(self.point)


   def moveTo(self, point):
       self.point = point
       self.visited.add(self.point)
