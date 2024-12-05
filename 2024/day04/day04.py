grid = []
cols = 0
rows = 0
otherMs = []


def read_grid():
    global grid
#    f = open("sample.txt")
    f = open("datas.txt")
#    f = open("sample2.txt")
    lines = f.readlines()
    grid = []
    for line in lines:
        grid.append(list(line.rstrip("\n")));
    f.close()


def left(x, y):
    global grid
    if x < 3:
        return 0
    return 1 if grid[y][x] == 'X' and grid[y][x-1] == 'M' and grid[y][x-2] == 'A' and grid[y][x-3] == 'S' else 0


def right(x, y):
    global grid
    if len(grid[y]) - x < 4:
        return 0
    return 1 if grid[y][x+1] == 'M' and grid[y][x+2] == 'A' and grid[y][x+3] == 'S' else 0


def northwest(x, y):
    global grid, rows, cols
    if x < 3 or y < 3:
        return 0
    return 1 if grid[y-1][x-1] == 'M' and grid[y-2][x-2] == 'A' and grid[y-3][x-3] == 'S' else 0


def northeast(x, y):
    global grid, cols
    if cols - x < 4 or y < 3:
        return 0
    return 1 if grid[y-1][x+1] == 'M' and grid[y-2][x+2] == 'A' and grid[y-3][x+3] == 'S' else 0


def southeast(x, y):
    global grid, rows, cols
    if cols - x < 4 or rows - y < 4:
        return 0
    return 1 if grid[y+1][x+1] == 'M' and grid[y+2][x+2] == 'A' and grid[y+3][x+3] == 'S' else 0


def southwest(x, y):
    global grid, rows, cols
    if x < 3 or rows - y < 4:
        return 0
    return 1 if grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == 'S' else 0

def up(x, y):
    global grid
    if y < 3:
        return 0
    return 1 if grid[y-1][x] == 'M' and grid[y-2][x] == 'A' and grid[y-3][x] == 'S' else 0


def down(x, y):
    global grid
    if len(grid) - y < 4:
        return 0
    return 1 if grid[y+1][x] == 'M' and grid[y+2][x] == 'A' and grid[y+3][x] == 'S' else 0


def count_xmas():
    global grid, rows, cols
    count = 0
    rows = len(grid)
    cols = len(grid[0])
    for y in range(0, rows):
        for x in range(0, cols):
            if grid[y][x] == 'X':
                count += left(x, y)
                count += northwest(x, y)
                count += up(x, y)
                count += northeast(x, y)
                count += right(x, y)
                count += southeast(x, y)
                count += down(x, y)
                count += southwest(x, y)
    return count

def used(mOne, mTwo):
    global otherMs
    found = list(filter((lambda mlist: (mlist[0] == mOne and mlist[1] == mTwo) or (mlist[0] == mTwo and mlist[1] == mOne)), otherMs))
    return len(found) > 0


## could be of pattern:
## M -
### yick... look at an M.
### he needs an M with a buffer either up, down, left or right

###               *
###
###             * M *
###
###               *
### of each of those directions, there's two mirror possibiltie.
#
# up you could have:     s  M'            M's
#                         a       or...    a
#                        s  M             M s

def check_at_top(x, y):
    global grid, cols, rows
    #bounds first...
    try:
        if used((x,y), (x, y-2)):
            return 0

        # math is safe now.
        if (grid[y-2][x] == 'M' and grid[y-1][x-1] == 'A' and grid[y-2][x-2] == 'S' and grid[y][x-2] == 'S' and y >= 2) or \
           (grid[y-2][x] == 'M' and grid[y-1][x+1] == 'A' and grid[y-2][x+2] == 'S' and grid[y][x+2] == 'S' and y >= 2):
            otherMs.append([(x,y),(x, y-2)])
            print(f"got a top {x}, {y}")
            return 1
    except:
        print("whoops")

    return 0



# s s
#  a
# m M   or....  m M
#                a
#               s s
def check_at_left(x, y):
    global grid, cols, rows
    #bounds first
    try:
        if used((x, y), (x-2, y)):
            return 0

        if (grid[y][x-2] == 'M' and grid[y - 1][x - 1] == 'A' and grid[y-2][x-2] == 'S' and grid[y-2][x] == 'S' and x >= 2) or \
           (grid[y][x-2] == 'M' and grid[y + 1][x - 1] == 'A' and grid[y+2][x-2] == 'S' and grid[y+2][x] == 'S' and x >= 2):
            otherMs.append([(x,y),(x-2, y)])
            print(f"got a left {x}, {y}")
            return 1
    except:
        print("whoops")

    return 0


# s s
#  a
# M m   or....  M m
#                a
#               s s

def check_at_right(x, y):
    global grid, cols, rows
    #bounds first
    try:
        if used((x,y), (x+2, y)):
            return 0

        if (grid[y][x+2] == 'M' and grid[y-1][x+1] == 'A' and grid[y-2][x] == 'S' and grid[y-2][x+2] == 'S') or \
           (grid[y][x+2] == 'M' and grid[y+1][x+1] == 'A' and grid[y+2][x] == 'S' and grid[y+2][x+2] == 'S'):
            otherMs.append([(x,y),(x+2, y)])
            print(f"got a right {x}, {y}")
            return 1
    except:
        print("whoops")

    return 0

#
# up you could have:     s M            M s
#                         a       or...  a
#                        s m            m s

def check_at_bottom(x, y):
    global grid, cols, rows
    #bounds first...
    try:
        if used((x, y), (x, y+2)):
            return 0

        # math is safe now.
        if (grid[y+2][x] == 'M' and grid[y+1][x-1] == 'A' and grid[y+2][x-2] == 'S' and grid[y+2][x] == 'S') or \
           (grid[y+2][x] == 'M' and grid[y+1][x+1] == 'A' and grid[y+2][x+2] == 'S' and grid[y+2][x] == 'S'):
            otherMs.append([(x,y),(x, y+2)])
            print(f"got a bottom {x}, {y}")
            return 1
    except:
        print("whoops")

    return 0


def count_mas():
    global grid, rows, cols
    count = 0
    for y in range(0, rows):
        for x in range(0, cols):
            if grid[y][x] == 'M':
                 count += check_at_top(x, y)
                 count += check_at_right(x, y)
                 count += check_at_left(x, y)
                 count += check_at_bottom(x, y)

    return count

def use_a():
    global grid, rows, cols
    ts = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    exes = 0
    for y in range(1, rows-1):
        print(f"YYYYYYYYYYYYYYYYYYY is: {y}")
        for x in range(1, cols-1):
            if grid[y][x] == 'A':
                str1 = grid[y-1][x-1] + 'A' + grid[y+1][x+1]
                str2 = grid[y+1][x-1] + 'A' + grid[y-1][x+1]
                if (str1 == 'MAS' or str1 == 'SAM') and (str2 == 'MAS' or str2 == 'SAM'):
                    exes += 1
    return exes



if __name__ == '__main__':
    read_grid()
    xmaseseseses = count_xmas()
    print(f"got these ones: {xmaseseseses} for part 1")
#    masses = count_mas()
#    print(f"got me these here many mas x's for part 2: {masses}")
    a_count = use_a()
    print(f"with a approach though... I'm sportin: {a_count}")


## part1 answer:  2639

## par2 1848 is toooooo low
## part 2 1860 tooo low.
## part 2 2072 too high
## part 2 2005 .. yeah??