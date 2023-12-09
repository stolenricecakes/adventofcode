import re

def read_file():
    f = open("input.txt", "r")
    #f = open("sample.txt", "r")
    lines = f.readlines()
    addRE = re.compile("^addx ([\-0-9]+)")
    instructions = [0] * (2 * len(lines))
    instructions[0] = 1
    i = 0
    for line in lines:
        line = line.rstrip("\n")
        add_result = addRE.search(line)
        if line == 'noop':
            print(f"nothing to do on line {i}")
            i += 1
        elif add_result:
            instructions[i+1] += int(add_result.group(1))
            i += 2
        else:
            print(f"what in the butts is {line}?")

    f.close()
    return instructions


def sum_values(instructions):
    tot = 0
    values = [20, 60, 100, 140, 180, 220]
    for val in values:
        reg = sum(instructions[0:val-1])
        tot += (reg * val)

    return tot


def determine_image(instructions):
    display = []
    for i in range(1, 241):
        register = sum(instructions[0:i-1])
        horiz = (i - 1) % 40
        if abs(horiz-register) <= 1:
            display.append("#")
        else:
            display.append(".")

    return display


def show_image(image):
    lines = [0, 40, 80, 120, 160, 200, 240]
    for i in range(1, len(lines)):
        stuffs = image[lines[i-1]:lines[i]]
        str = "".join(stuffs)
        print(f"{str}")


if __name__ == '__main__':
    instructions = read_file()
    total_val = sum_values(instructions)
    print(f"yo bro - your tot is: {total_val}")
    image = determine_image(instructions)
    show_image(image)

#it says: 1 + 15 - 11 + 6 - 3 + 5 - 1 - 8 + 13 + 4