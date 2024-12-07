class Feller:
    direction_dict = {"up": 1, "right": 2, "down": 4, "left": 8}
    next_direction = {"up": "right", "right": "down", "down": "left", "left": "up"}
    x = 0
    y = 0
    direction = "up"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = "up"

    def next_spot(self):
        if self.direction == "up":
            return (self.x, self.y-1)
        elif self.direction == "right":
            return (self.x + 1, self.y)
        elif self.direction == "down":
            return (self.x, self.y+1)
        else:
            return (self.x - 1, self.y)


    def move(self):
        next = self.next_spot()
        self.x = next[0]
        self.y = next[1]

    def current_position(self):
        return (self.x, self.y)


    def get_direction_val(self):
        return self.direction_dict[self.direction]

    def turn(self):
        self.direction = self.next_direction[self.direction]