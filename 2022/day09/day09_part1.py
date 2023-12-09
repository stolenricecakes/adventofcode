from knot import *

head = Knot("head")
tail = Knot("tail")

def read_stuff():
    f = open("input.txt", "r")
    #f = open("sample.txt", "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip("\n")

    f.close()
    return lines


def move_left(steps):
    global head
    global tail
    for i in range(0, steps):
        head.moveTo(head.point.left())
        if not head.point.touching(tail.point):
            tail.moveTo(Point(head.point.x + 1, head.point.y))


def move_up(steps):
    global head
    global tail
    for i in range(0, steps):
        head.moveTo(head.point.up())
        if not head.point.touching(tail.point):
            tail.moveTo(Point(head.point.x, head.point.y - 1))


def move_down(steps):
    global head
    global tail
    for i in range(0, steps):
        head.moveTo(head.point.down())
        if not head.point.touching(tail.point):
            tail.moveTo(Point(head.point.x, head.point.y + 1))



def move_right(steps):
    global head
    global tail
    for i in range(0, steps):
        head.moveTo(head.point.right())
        if not head.point.touching(tail.point):
            tail.moveTo(Point(head.point.x - 1, head.point.y))



def process_moves(moves):
    global tail
    for move in moves:
        parts = move.split(" ")
        if parts[0] == 'L':
            move_left(int(parts[1]))
        elif parts[0] == 'U':
            move_up(int(parts[1]))
        elif parts[0] == 'R':
            move_right(int(parts[1]))
        elif parts[0] == 'D':
            move_down(int(parts[1]))
        else:
            print(f"WHAT IN the vomit is {parts[0]}?  can't move that way.")

    print(f"all done moving now.")
    print(f" tail has visited {len(tail.visited)} points.")
    print(f"points visited:\n\n {tail.visited}")


if __name__ == '__main__':
    moves = read_stuff()
    process_moves(moves)

