import re

def read_lines():
#    f = open("sample.txt")
    f = open("datas.txt")
    lines = f.readlines()
    clean_lines = []
    for line in lines:
        clean_lines.append(line.rstrip("\n"));
    f.close()
    return clean_lines


def part1(lines):
    total = 0
    multRE = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)");
    for line in lines:
        for result in multRE.finditer(line):
            print(f"resulty: {result}")
            total += int(result.group(1)) * int(result.group(2))
            print(f" total is now: {total}\n")
    return total


if __name__ == '__main__':
    lines = read_lines()
    part1_total = part1(lines)
    print(f"oh my toots!, the total for part1 is: {part1_total}")