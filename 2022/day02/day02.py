

def calc_throw_score(us):
    return ord(us) - ord("X") + 1

def calc_win_score(themStr, usStr):
    them = ord(themStr) - ord("A")
    us = ord(usStr) - ord("X")

    if us == them:
        return 3
    elif us - them == 1 or us - them == -2:
        return 6
    else:
        return 0

def part2_calc_score(usStr):
    us = ord(usStr) - ord("X")
    return us * 3

def part2_calc_throw(themStr, usStr):
    them = ord(themStr) - ord("A")
    us = ord(usStr) - ord("X")
    card = them
    if us == 0:
        ## we need to throw one less.
        card = them - 1
        if card < 0:
            card = 2
    elif us == 2:
        ## we need to throw one more
        card = them + 1
        if them >= 2:
            card = 0


    return card + 1


def do_stuff():
    f = open("input.txt", "r")
    lines = f.readlines()
    total_score = 0
    for line in lines:
        split_ary = line.rstrip("\n").split(" ")
        them = split_ary[0]
        us = split_ary[1]
#        throw_score = calc_throw_score(us)
#        win_score = calc_win_score(them, us)
        throw_score = part2_calc_throw(them, us)
        win_score = part2_calc_score(us)
        total_score += throw_score + win_score


    print(f"oh baby - total score is: {total_score}")
    f.close()

### total score of 8439 is too high... hmm...

if __name__ == '__main__':
    do_stuff()

