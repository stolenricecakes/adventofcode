import string


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def get_alpha_score(letter):
    l = list(string.ascii_letters)
    return l.index(letter) + 1

def do_things():
    f = open("input.txt", "r")
#    f = open("fart.txt", "r")
    lines = f.readlines()
    total_score = 0
    for line in lines:
        line = line.rstrip("\n")
        half_length = int(len(line) / 2)
        first_compartment = line[0:half_length]
        second_compartment = line[half_length:]
        list1 = list(first_compartment)
        list2 = list(second_compartment)
        common = intersection(list1, list2)
        print(f"have this in common: {common}")
        score = get_alpha_score(common[0])
        print(f" score is: {score} ")
        total_score += score

    print(f"total score is: {total_score}")

    f.close()

def part2_do_things():
    list_group = [];
    f = open("input.txt", "r")
    lines = f.readlines()
    total_score = 0
    for line in lines:
        line = line.rstrip("\n")
        list_group.append(list(line))
        if (len(list_group)) == 3:
            first_list = intersection(list_group[0], list_group[1])
            common = intersection(first_list, list_group[2])
            print(f"common of {list_group} is {common}")
            score = get_alpha_score(common[0])
            total_score += score
            print(f"score is {score} from the common {common} of {list_group}")
            list_group.clear()

    print(f"list group has: {len(list_group)}")
    print(f"total score is: {total_score}")
    f.close()



if __name__ == '__main__':
    #do_things()
    part2_do_things()
