# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_in_file():
    # Use a breakpoint in the code line below to debug your script.
    f = open("input.txt", "r")
    lines = f.readlines()
    elves = [0]
    for line in lines:
        if line == "\n":
            elves.append(0)
        else:
            elfTot = elves.pop()
            elfTot += int(line.rstrip("\n"))
            elves.append(elfTot)

    ## these are the top 3 elves:
    #   67758, 67958, 74198

    sorted_elves = sorted(elves, reverse=True)
    print(f"top elf is: {sorted_elves}\n\n")

    three_elves = sorted_elves[0:3]

    print(f"top 3 elves are: {three_elves}\n\n")

    elf_sum = sum(three_elves)

    print(f"yo the top 3 elves total: {elf_sum}")

    f.close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_in_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
