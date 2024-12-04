grid = []
cols = 0
rows = 0

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
    global grid
    global cols
    global rows
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


#def count_mas(grid):
#    pass


if __name__ == '__main__':
    read_grid()
    xmaseseseses = count_xmas()
    print(f"got these ones: {xmaseseseses} for part 1")
#    masses = count_mas(grid)


## part1 answer:  2639
