

def part_one():
#    f = open("sampledata.txt", "r")
    f = open("data.txt", "r")
    lines = f.readlines()
    left = []
    right = []
    for line in lines:
        splito = line.rstrip("\n").split(" ")
        left.append(int(splito[0]))
        right.append(int(splito[len(splito) - 1]))

    right = sorted(right)
    left = sorted(left)

    diff = 0
    for i in range(0, len(left)):
        diff += abs(left[i] - right[i])

    print(f"diff is: {diff}")


def part_two():
    #f = open("sampledata.txt", "r")
    f = open("data.txt", "r")
    lines = f.readlines()
    left = []
    right = []
    for line in lines:
        splito = line.rstrip("\n").split(" ")
        left.append(int(splito[0]))
        right.append(int(splito[len(splito) - 1]))

    similar = 0
    for val in left:
       c = right.count(val)
       similar += (val * c)

    print (f"similar is: {similar}")


if __name__ == '__main__':
#    part_one()
    part_two()