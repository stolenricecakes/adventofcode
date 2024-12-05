from functools import cmp_to_key

forward_rules = []
backward_rules = []
desired_prints = []
sortos = []
legit = []


def read_stuff():
    global forward_rules, backward_rules, desired_prints
#    f = open("sample.txt")
    f = open("datas.txt")
#    f = open("sample2.txt")
    lines = f.readlines()
    for blurg in lines:
        line = blurg.rstrip("\n")
        if len(line) > 0:
            if "|" in line:
               splitty = line.split("|")
               forward_rules.append((int(splitty[0]), int(splitty[1])))
               backward_rules.append((int(splitty[1]), int(splitty[0])))
            else:
               printy = list(map((lambda l: int(l)) ,line.split(",")))
               desired_prints.append(printy)

    f.close()

def sorto(num1, num2):
    ## do we have forward?
    have_forward =  len(list(filter((lambda l: l[0] == num1 and l[1] == num2), forward_rules))) > 0
    if have_forward:
        print(f"holy farties, {num1} comes before {num2}")
        return -1

    have_backward =  len(list(filter((lambda l: l[0] == num1 and l[1] == num2), backward_rules))) > 0
    if have_backward:
        print(f"wowzers, {num1} comes AFTER {num2}")
        return 1

    print(f"I aint know squat about {num1} and {num2}")
    return 0


def sortman(ary):
    return ary.sort(key=cmp_to_key(sorto))


def woo():
    print(f"f rules: {forward_rules}")
    print(f"b rules: {backward_rules}")
    print(f"desired: {desired_prints}")


def find_legit():
    global legit
    for printy in desired_prints:
        sorty = printy.copy()
        sortman(sorty)
        if printy == sorty:
            legit.append(printy)
        else:
            print(f"{printy} is total trash")

def add_legit():
    total = 0
    for l in legit:
        middle = int(len(l) / 2)
        print(f"middle is: {middle}")
        total += l[middle]
        print(f"total is now: {total}")
    return total


def wowzo():
    global sortos
    for printy in desired_prints:
        #print(f"\n\n\tprinty: {printy}")
        sorty = printy.copy()
        sortman(sorty)
        sortos.append(sorty)
        print(f"\tprintyagain: {sorty}")


def middle_out():
    global sortos
    total = 0
    for sorty in sortos:
        middle = int(len(sorty) / 2)
        print(f"middle is: {middle}")
        total += sorty[middle]
        print(f"total is now: {total}")

    return total


if __name__ == '__main__':
    read_stuff()
    woo()
    find_legit()
    total = add_legit()
    print(f" yo bro, sportin this total: \t{total}")
#    wowzo()
#    total = middle_out()
#    print(f"hey there total is: {total}")


### fartles, 12020 is too high
### 7307 for part1.