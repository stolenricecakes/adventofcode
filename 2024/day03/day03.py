import re

def read_lines():
#    f = open("sample.txt")
    f = open("datas.txt")
#    f = open("sample2.txt")
    lines = f.readlines()
    clean_lines = []
    for line in lines:
        clean_lines.append(line.rstrip("\n"));
    f.close()
    return clean_lines


def part1(lines):
    total = 0
    multRE = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)")
    for line in lines:
        for result in multRE.finditer(line):
            print(f"resulty: {result}")
            total += int(result.group(1)) * int(result.group(2))
            print(f" total is now: {total}\n")
    return total


def is_enabled(enabled_ranges, value):
    ranges = list(filter((lambda t : t[0] <= value <= t[1]), enabled_ranges))
    return len(ranges) > 0


def part2(lines):
    total = 0
    multRE = re.compile("mul\\((\\d{1,3}),(\\d{1,3})\\)")
    dodontRE = re.compile("(do\\(\\)|don't\\(\\))")
    enabled = True
    for line in lines:
        enabledRanges = []
        lastEnable = 0
        onoffs = dodontRE.finditer(line)
        for onoff in onoffs:
            print(f"onoffy: {onoff}")
            if onoff.group(1).find("don") == 0:
               if enabled:
                   enabledRanges.append((lastEnable, onoff.span()[0]))
                   enabled = False
            else:
               if not enabled:
                   enabled = True
                   lastEnable = onoff.span()[1]
        if enabled:
           enabledRanges.append((lastEnable, len(line)))

        print(f"ranges: {enabledRanges}")

        for result in multRE.finditer(line):
            # print(f"resulty: {result}")
            if is_enabled(enabledRanges, result.span()[0]):
                total += int(result.group(1)) * int(result.group(2))
                print(f" total is now: {total}\n")
            else:
                print(f" result ({result.group(1)},{result.group(2)}) at {result.span()[0]} aint even enabled.")

    return total


if __name__ == '__main__':
    lines = read_lines()
    #part1_total = part1(lines)
    #print(f"oh my toots!, the total for part1 is: {part1_total}")
    part2_total = part2(lines)
    print(f"holy macorole! part2 total is: {part2_total}")

