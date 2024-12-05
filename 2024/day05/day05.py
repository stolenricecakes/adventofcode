from functools import cmp_to_key

forward_rules = []
backward_rules = []
desired_prints = []
fixed = []
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
            fixed.append(sorty)
            print(f"{printy} is total trash, but fixed it to {sorty}")


def sum_the_middles(printos):
    total = 0
    for printy in printos:
        middle = int(len(printy) / 2)
        total += printy[middle]
    return total


if __name__ == '__main__':
    read_stuff()
    woo()
    find_legit()
    legitTotal = sum_the_middles(legit)
    print(f" yo bro, sportin this part 1 total: \t{legitTotal}")
    fixedTotal = sum_the_middles(fixed)
    print(f" 💩 sportin this part 2 total: \t{fixedTotal}")


### fartles, 12020 is too high
### 7307 for part1.
## 4713 part 2?