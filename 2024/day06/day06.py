import feller

grid = []
rows = 0
cols = 0
visited = {}
barracades = []
visited_ary = []

def read_stuff():
    global grid, rows, cols
#    f = open("sample.txt")
    f = open("datas.txt")
    lines = f.readlines()
    for blurg in lines:
        line = blurg.rstrip("\n")
        grid.append(list(line))
    rows = len(grid)
    cols = len(grid[0])
    f.close()

def make_feller():
    for y in range(0, rows):
        for x in range(0, cols):
            if grid[y][x] == '^':
               return feller.Feller(x, y)


def initalize_visited_ary():
    global visited_ary
    visited_ary = []
    for y in range(0, rows):
        visited_ary.append([])
        for x in range(0, cols):
            visited_ary[y].append(0)



def walk_the_grid(fella):
    global grid, visited, barracades
    visit_spot(fella, "^")
    stff = fella.current_position()
    grid[stff[1]][stff[0]] = "X"

    nextspot = fella.next_spot()

    while 0 <= nextspot[0] < cols and 0 <= nextspot[1] < rows:
        gridval = grid[nextspot[1]][nextspot[0]]

        rightval = fella.get_right_val()
        loop_here=False
        right_slice = get_right_slice(fella)
        for i in range (0, len(right_slice)):
            if right_slice[i] & rightval == rightval:
                print(f"HOLY MOLE GUACAMOLE!  I found me a loop at rightslice # {i}")
                loop_here = True
                add_to_right_slice(fella, rightval)

#        rightval = fella.get_right_val()
#        right_key = str(on_right[0]) + "," + str(on_right[1])
#        print(f"visiting: {fella.current_position()} right is: {on_right}, key: {right_key}")
#        if right_key in visited:
#            print(f"right key in visited as: {visited[right_key]} and rightval: {rightval}")
#        if right_key in visited and (visited[right_key] & rightval) == rightval:
        if loop_here:
            on_right = fella.get_spot_on_right()
            print(f"HOLY CRAPDUMPS!!!")
            print(f"I'm at {fella.current_position()} and there's poop on the line to my right: {on_right}")
            print(f"put a barracade at: {nextspot} ")
            barracades.append(nextspot)

        if gridval == "#":
            fella.turn()
        else:
            fella.move()
            visit_spot(fella, gridval)
            if gridval == ".":
                grid[nextspot[1]][nextspot[0]] = 'X'
        nextspot = fella.next_spot()

    print(f"off the grid at nextspot: {nextspot[0]}, {nextspot[1]}")


def visit_spot(fella, symbol):
    global visited
    spot = fella.current_position()
    key = str(spot[0]) + "," + str(spot[1])
    visited_ary[spot[1]][spot[0]] |= fella.get_direction_val()

    if symbol == '.' or symbol == '^':
        visited[key] = fella.get_direction_val()
    elif symbol == 'X':
        visited[key] |= fella.get_direction_val()


def print_summary(fella):
    print(f"visited the following spots: {visited}")
    print(f"total of {len(visited)}")
    print(f"\n\nbarracades at: {barracades}")
    print(f"total of {len(barracades)}")


def get_right_slice(fella):
    global grid
    global visited_ary
    right_slice = []
    rdir = fella.get_right_direction()
    pos = fella.current_position()
    if rdir == "up":
        for i in range(pos[1]+1, -1, -1):
            right_slice.append(visited_ary[i][pos[0]])
        for i in range(pos[1]-1, rows):
            if grid[i][pos[0]] != "#":
                right_slice.append(visited_ary[i][pos[0]])
            else:
                break
    elif rdir == "right":
        for i in range(pos[0]+1, cols):
            right_slice.append(visited_ary[pos[1]][i])
        for i in range(pos[0]-1, -1, -1):
            if grid[pos[1]][i] != "#":
                right_slice.append(visited_ary[pos[1]][i])
            else:
                break
    elif rdir == "down":
        for i in range(pos[1]+1, rows):
            right_slice.append(visited_ary[i][pos[0]])
        for i in range(pos[1] - 1, -1, -1):
            if grid[i][pos[0]] != "#":
                right_slice.append(visited_ary[i][pos[0]])
            else:
                break
    else:
        for i in range(pos[0]-1, -1, -1):
            right_slice.append(visited_ary[pos[1]][i])
        for i in range(pos[0]+1, cols):
            if grid[pos[1]][i] != "#":
                right_slice.append(visited_ary[pos[1]][i])
            else:
                break

    return right_slice


def add_to_right_slice(fella, rightval):
    global visited_ary
    rdir = fella.get_right_direction()
    pos = fella.current_position()
    if rdir == "up":
        for i in range(pos[1], -1, -1):
            visited_ary[i][pos[0]] |= rightval
    elif rdir == "right":
        for i in range(pos[0], cols):
            visited_ary[pos[1]][i] |= rightval
    elif rdir == "down":
        for i in range(pos[1], rows):
            visited_ary[i][pos[0]] |= rightval
    else:
        for i in range(pos[0], -1, -1):
            visited_ary[pos[1]][i] |= rightval



if __name__ == '__main__':
    read_stuff()
    initalize_visited_ary()
    fella = make_feller()
    walk_the_grid(fella)
    print_summary(fella)


## part 1: 5564
## part 2: 867 too low farties.
## part 2: 992 too low (marking all the right slices as visited)
## part 2: 992 - even going the opposite of the right direction looking for others with the same value.