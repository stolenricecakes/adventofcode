import feller

grid = []
rows = 0
cols = 0
visited = {}

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


def walk_the_grid(fella):
    global grid
    visit_spot(fella, "^")
    stff = fella.current_position()
    grid[stff[1]][stff[0]] = "X"

    nextspot = fella.next_spot()

    while 0 <= nextspot[0] < cols and 0 <= nextspot[1] < rows:
        gridval = grid[nextspot[1]][nextspot[0]]
        print(f"at: {gridval}")
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
    if symbol == '.' or symbol == '^':
        visited[key] = fella.get_direction_val()
    elif symbol == 'X':
        visited[key] |= fella.get_direction_val()




def print_summary(fella):
    print(f"visited the following spots: {visited}")
    print(f"total of {len(visited)}")


if __name__ == '__main__':
    read_stuff()
    fella = make_feller()
    walk_the_grid(fella)
    print_summary(fella)


## part 1: 5564