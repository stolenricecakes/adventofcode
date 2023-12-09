##f = open("input.txt", "r")
##    f = open("teeny_test.txt", "r")
def read_in_matrix():
    f = open("input.txt", "r")
    lines = f.readlines()
    matrix = []
    for line in lines:
        line = line.rstrip("\n")
        row = list(line)
        introw = []
        for r in row:
            introw.append(int(r))
        matrix.append(introw)

    f.close()
    return matrix


def no_blockers(treelist, value):
    blockers = list(filter(lambda x: x >= value, treelist))
    return len(blockers) == 0


def visible_from_top(matrix, r, c):
    blockers = north_array(matrix, r, c)
    return no_blockers(blockers, matrix[r][c])


def visible_from_bottom(matrix, r, c):
    blockers = south_array(matrix, r, c)
    return no_blockers(blockers, matrix[r][c])


def visible_from_west(matrix, r, c):
    l = west_array(matrix, r, c)
    return no_blockers(l, matrix[r][c])


def visible_from_east(matrix, r, c):
    l = east_array(matrix, r, c)
    return no_blockers(l, matrix[r][c])


def west_array(matrix, r, c):
    l = matrix[r][0:c]
    l.reverse()
    return l


def east_array(matrix, r, c):
    return matrix[r][c+1:]


def south_array(matrix, r, c):
    blockers = []
    for i in range(r+1, len(matrix)):
        blockers.append(matrix[i][c])
    return blockers


def north_array(matrix, r, c):
    blockers = []
    for i in range(0, r):
        blockers.append(matrix[i][c])
    blockers.reverse()
    return blockers


def count_visibles(matrix):
    num_vis = (len(matrix) * 4) - 4  ## all the outsides
    for r in range(1, len(matrix) - 1):
        for c in range(1, len(matrix[r]) - 1):
           if visible_from_top(matrix, r, c) or \
              visible_from_bottom(matrix, r, c) or \
              visible_from_east(matrix, r, c) or \
              visible_from_west(matrix, r, c):
               num_vis += 1

    return num_vis


def distance(l, val):
    dist = 1
    for tree in l:
        if tree >= val:
            break
        else:
            dist += 1

    return min(dist,len(l))


def determine_scenery(matrix, r, c):
    val = matrix[r][c]
    north = distance(north_array(matrix, r, c), val)
    west = distance(west_array(matrix, r, c), val)
    south = distance(south_array(matrix, r, c), val)
    east = distance(east_array(matrix, r, c), val)
    return north * west * south * east


def find_most_scenic(matrix):
    most_scenic = 0
    for r in range(1, len(matrix) - 1):
        for c in range(1, len(matrix[r]) - 1):
            scenery = determine_scenery(matrix, r, c)
            if (scenery > most_scenic):
                print(f"dang!  new scenic sqaure of {scenery} at {r}x{c}")
                most_scenic = scenery

    return most_scenic


if __name__ == '__main__':
    matrix = read_in_matrix()
    visibles = count_visibles(matrix)
    ## 1293?? - NOPE its 1782.

    print(f"oh baby I can see {visibles} of {len(matrix) * len(matrix)} trees.")

    most_scenic = find_most_scenic(matrix)
    ## guessed 516672, but that's too high.
    print(f"holy tinkles!  most scenic square is {most_scenic}")




