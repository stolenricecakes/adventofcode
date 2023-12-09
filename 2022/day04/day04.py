
def list_from_range(strRange):
    range_arr = strRange.split("-");
    return list(range(int(range_arr[0]), int(range_arr[1]) + 1))


def completely_included(list1, list2):
    return (list1[0] >= list2[0] and list1[-1] <= list2[-1]) or (list2[0] >= list1[0] and list2[-1] <= list1[-1])


def any_overlap(list1, list2):
    return (list1[0] >= list2[0] and list1[0] <= list2[-1]) or \
           (list1[-1] >= list2[0] and list1[-1] <= list2[-1]) or \
           (list2[0] >= list1[0] and list2[0] <= list1[-1]) or \
           (list2[-1] >= list1[0] and list2[-1] <= list1[-1])

##
## if first list is inbetween
##


def read_stuff():
    f = open("input.txt", "r")
    lines = f.readlines()
    matchos = 0
    for line in lines:
        line_ary = line.rstrip("\n").split(",")
        first_group = list_from_range(line_ary[0])
        second_group = list_from_range(line_ary[1])
        if any_overlap(first_group, second_group):
            print(f"oh got some overlap: {first_group} and {second_group}")
            matchos = matchos + 1

#        if (completely_included(first_group, second_group)):
#            print(f"got a matcho - for {first_group} and {second_group}")
#            matchos = matchos + 1

    print(f"we're sportin {matchos} matcheritos")

    f.close()


if __name__ == '__main__':
    read_stuff()