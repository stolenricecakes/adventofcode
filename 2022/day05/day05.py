import re

stackLines = []
moves = []
numStacks = 0
stacks = None

def process_file():
    f = open("input.txt", "r")
    global numStacks
    global moves
    global stackLines
    stackRE = re.compile("^\[[A-Z]\]")
    numRE = re.compile("^\s\d\s")
    moveRE = re.compile("^move \d+ from \d to \d")
    lines = f.readlines();
    for line in lines:
        line = line.rstrip("\n")
        if stackRE.search(line):
            stackLines.append(line)
        elif numRE.search(line):
            numStacks = int(line.split(" ")[-1])
            print(f"oh baby I have {numStacks} stacks")
        elif moveRE.search(line):
            moves.append(line)
        else:
            print(f"what the tinkle is {line}")

    f.close()


def read_initial_stacks():
    global stacks
    #stacks = [[]] * numStacks
    stacks = [[] for _ in range(numStacks)]
    stackLines.reverse()
    for stackLine in stackLines:
        stackLineList = list(stackLine)
        for x in range(0, numStacks):
            idx = (x * 4) + 1
            if (idx < len(stackLineList)):
                label = stackLineList[idx]
                if label != ' ':
                    stacks[x].append(label)
    print(f"{stacks}")



def process_moves():
    moveRE = re.compile("^move (\d+) from (\d) to (\d)")
    global moves
    global stacks
    for move in moves:
        result = moveRE.search(move)
        how_many = int(result.group(1))
        from_stack = int(result.group(2)) - 1
        to_stack = int(result.group(3)) - 1

        stack_from = stacks[from_stack]
        from_idx = len(stack_from) - how_many
        stuff_to_move = stack_from[from_idx::]
        stacks[from_stack] = stack_from[0:from_idx]
        # part 2... stuff_to_move.reverse()

        stack_to = stacks[to_stack]
        for thing in stuff_to_move:
            stack_to.append(thing)

    print(f"oh baby - stacks are {stacks}")


def print_poopies():
    #hey
    global stacks
    end_result = ''
    for stack in stacks:
        end_result = end_result + stack[-1]

    #should be... RNZLFZSJH
    print(f"final top of stack is: {end_result}")


if __name__ == '__main__':
    process_file()
    read_initial_stacks()
    process_moves()
    print_poopies()


