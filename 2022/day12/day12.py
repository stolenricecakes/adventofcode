from point import Point

dead_ends=[]

def read_file():
#    f = open("sample.txt", "r")
    f = open("input.txt", "r")
    lines = []
    for row in f.readlines():
        row = row.rstrip("\n");
        rowlist = list(row)
        lines.append(rowlist)

    return lines

def find_char(grid, what):
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid[row][col] == what:
                return Point(x=col, y=row)

    return None


def is_square_in_bounds(square, grid):
    if square.x < 0 or square.y < 0:
        return False
    elif square.x >= len(grid[0]):
        return False
    elif square.y >= len(grid):
        return False
    else:
        return True


def get_ord_for_square(square, grid):
    letter = grid[square.y][square.x]
    if letter == 'S':
        letter = '`' ## one before a.
    elif letter == 'E':
        letter = 'z'
    return ord(letter)


def is_eliv_lower_or_one_higher(current, square, grid):
    eliv_ord = get_ord_for_square(current, grid)
    eliv_square = get_ord_for_square(square, grid)
    return eliv_square - eliv_ord <= 1


def find_possible_squares(current, grid):
    possibles = []
    for square in [Point(current.x, current.y - 1), Point(current.x, current.y + 1), Point(current.x - 1, current.y), Point(current.x + 1, current.y)]:
        if is_square_in_bounds(square, grid) and \
           is_eliv_lower_or_one_higher(current, square, grid):
            square.eliv = grid[square.y][square.x]
            possibles.append(square)

    return possibles



def find_better_square(current, end, grid, visited):
    global dead_ends

    possible = []
    for pos in find_possible_squares(current, grid):
        if not pos in visited and not pos in dead_ends:
            possible.append(pos)

    if len(possible) == 0:
        dead_ends.append(current)
        visited.pop(-1)
        return visited[-1]
    else:
        for p in possible:
            p.distance_between(end)

        possible.sort(key=lambda m: (m.eliv, -m.dist), reverse=True)

        return possible[0]


def explore(grid, start, end):
    path = [start]
    better = find_better_square(start, end, grid, path)
    while better.x != end.x or better.y != end.y:
        if not better in path:
            path.append(better)
        better = find_better_square(better, end, grid, path)
        print(f"what about adding {better} to path?")

    print(f"holy farties! just found the path: {path}")
    print(f"its {len(path)} long")


if __name__ == '__main__':
    grid = read_file()
    start = find_char(grid, 'S')
    end = find_char(grid, 'E')
    explore(grid, start, end)
    print("poopies")
