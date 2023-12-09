from knot import *
import matplotlib.pyplot as plt

chain = []

def read_stuff():
    f = open("input.txt", "r")
    #f = open("sample.txt", "r")
    #f = open("sample2.txt", "r")
    lines = f.readlines()
    for line in lines:
        line = line.rstrip("\n")

    f.close()
    return lines


def move_left(steps):
    global chain
    for q in range(0, steps):
        chain[0].moveTo(chain[0].point.left())
        for i in range(1, len(chain)):
            change = determine_change_needed(chain[i-1], chain[i])
            if change.x == 0 and change.y == 0:
                print("doing nothin")
            else:
                chain[i].moveTo(Point(chain[i].point.x + change.x, chain[i].point.y + change.y))
            ### hacking...
            #if not chain[i - 1].point.touching(chain[i].point):
            #    if chain[i - 1].point.diagonal(chain[i].point):
            #        if chain[i].point.y < chain[i - 1].point.y:
            #            chain[i].moveTo(Point(chain[i].point.x - 1, chain[i].point.y + 1))
            #        else:
            #            chain[i].moveTo(Point(chain[i].point.x - 1, chain[i].point.y - 1))
            #    else:
            #        chain[i].moveTo(Point(chain[i].point.x - 1, chain[i].point.y))


def move_up(steps):
    global chain
    for q in range(0, steps):
        chain[0].moveTo(chain[0].point.up())
        for i in range(1, len(chain)):
            change = determine_change_needed(chain[i - 1], chain[i])
            if change.x == 0 and change.y == 0:
                print("doing nothin")
            else:
                chain[i].moveTo(Point(chain[i].point.x + change.x, chain[i].point.y + change.y))

#        for i in range(1, len(chain)):
#            if not chain[i-1].point.touching(chain[i].point):
#                if chain[i-1].point.diagonal(chain[i].point):
#                    if chain[i].point.x < chain[i-1].point.x:
#                        chain[i].moveTo(Point(chain[i].point.x + 1, chain[i].point.y + 1))
#                    else:
#                        chain[i].moveTo(Point(chain[i].point.x - 1, chain[i].point.y + 1))
#                else:
#                    chain[i].moveTo(Point(chain[i].point.x, chain[i].point.y + 1))


def move_down(steps):
    global chain
    for q in range(0, steps):
        chain[0].moveTo(chain[0].point.down())
        for i in range(1, len(chain)):
            change = determine_change_needed(chain[i - 1], chain[i])
            if change.x == 0 and change.y == 0:
                print("doing nothin")
            else:
                chain[i].moveTo(Point(chain[i].point.x + change.x, chain[i].point.y + change.y))

#        for i in range(1, len(chain)):
#            if not chain[i - 1].point.touching(chain[i].point):
#                if chain[i - 1].point.diagonal(chain[i].point):
#                    if chain[i].point.x < chain[i - 1].point.x:
#                        chain[i].moveTo(Point(chain[i].point.x + 1, chain[i].point.y - 1))
#                    else:
#                        chain[i].moveTo(Point(chain[i].point.x - 1, chain[i].point.y - 1))
#                else:
#                    chain[i].moveTo(Point(chain[i].point.x, chain[i].point.y - 1))


def move_right(steps):
    global chain
    for i in range(0, steps):
        chain[0].moveTo(chain[0].point.right())
        for i in range(1, len(chain)):
            change = determine_change_needed(chain[i - 1], chain[i])
            if change.x == 0 and change.y == 0:
                print("doing nothin")
            else:
                chain[i].moveTo(Point(chain[i].point.x + change.x, chain[i].point.y + change.y))
#        for c in range(1, len(chain)):
#            if not chain[c - 1].point.touching(chain[c].point):
#                if chain[c - 1].point.diagonal(chain[c].point):
#                    if chain[c].point.y < chain[c - 1].point.y:
#                        chain[c].moveTo(Point(chain[c].point.x + 1, chain[c].point.y + 1))
#                    else:
#                        chain[c].moveTo(Point(chain[c].point.x + 1, chain[c].point.y - 1))
#                else:
#                    chain[c].moveTo(Point(chain[c].point.x + 1, chain[c].point.y))

def determine_change_needed(head, tail):
    if head.point.touching(tail.point):
        return Point(0, 0)

    if head.point.diagonal(tail.point):
        ## determine if were horiz or vert
        if head.point.x - tail.point.x > 0:
            new_x = 1
        else:
            new_x = -1

        if head.point.y - tail.point.y > 0:
            new_y = 1
        else:
            new_y = -1

        return Point(new_x, new_y)
    else:
        if head.point.y > tail.point.y:
            return Point(0, 1)
        elif head.point.y < tail.point.y:
            return Point(0, -1)
        elif head.point.x > tail.point.x:
            return Point(1, 0)
        else:
            return Point(-1, 0)


def process_moves(moves):
    global chain
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
        #show_current()

    print(f"all done moving now.")
    print(f" tail has visited {len(chain[-1].visited)} points.")
    print(f"points visited:\n\n {chain[-1].visited}")


def show_current():
    global chain
    x = []
    y = []
    for link in chain:
        x.append(link.point.x)
        y.append(link.point.y)

    plt.scatter(x, y)
    plt.show()


def plot_moves():
    global chain
    x = []
    y = []
    for dot in chain[-1].visited:
        x.append(dot.x)
        y.append(dot.y)

    plt.scatter(x, y)
    plt.show()
    print("tinkle")




if __name__ == '__main__':
    moves = read_stuff()
    for a in range(0, 10):
        chain.append(Knot(name=a))
    process_moves(moves)
    plot_moves()

