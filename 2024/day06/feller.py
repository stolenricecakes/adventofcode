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
        return self.next_spot_with_direction(self.direction)

    def next_spot_with_direction(self, dir):
        if dir == "up":
            return (self.x, self.y-1)
        elif dir == "right":
            return (self.x + 1, self.y)
        elif dir == "down":
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

    def get_right_val(self):
        return self.direction_dict[self.next_direction[self.direction]]

    def turn(self):
        self.direction = self.next_direction[self.direction]

    def get_right_direction(self):
        return self.next_direction[self.direction]

    def get_spot_on_right(self):
        next_dir = self.next_direction[self.direction]
        return self.next_spot_with_direction(next_dir)
