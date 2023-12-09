import re
import node

def read_file():
    input = open("input.txt", "r")
    cdCmd = re.compile("^\$ cd ([\./a-z]+)")
    lsCmd = re.compile("^\$ ls")
    fileRe = re.compile("^([\d]+)\s(.+)")
    dirRe = re.compile("^dir\s(.+)")
    lines = input.readlines()
    rootNode = node.Node(isDirectory=True, name="/")
    currentNode = rootNode
    for line in lines:
        line = line.rstrip("\n")
        cd = cdCmd.search(line)
        ls = lsCmd.search(line)
        f = fileRe.search(line)
        d = dirRe.search(line)

        if cd:
            newDir = cd.group(1)
            if newDir == '/':
                currentNode = rootNode
            elif newDir == '..':
                currentNode = currentNode.parent
            else:
                currentNode = currentNode.children[newDir]
        elif ls:
            ## this is really a no-op.
            print("ls is the coolest")
        elif f:
            newFile = node.Node(parent=currentNode, isDirectory=False, name=f.group(2), size=int(f.group(1)))
            currentNode.children[newFile.name] = newFile
        elif d:
            newDir = node.Node(parent=currentNode, isDirectory=True, name=d.group(1))
            currentNode.children[newDir.name] = newDir
        else:
            print(f"holy stinkin crap - I don't know {line}")


    input.close()
    return rootNode


def calc_sizes(rootNode):
    big_ol_size = rootNode.getSize()
    print(f"all the trees add up to: {big_ol_size}")


def find_all_dirs_less_than(rootNode, cutoff):
    all_dirs = []
    get_all_dirs(all_dirs, rootNode)
    print(f"I got {len(all_dirs)} dirs")
    smaller_dirs = []
    for dir in all_dirs:
        if dir.calculatedSize <= cutoff:
            smaller_dirs.append(dir)

    return smaller_dirs


def get_all_dirs(listy, node):
    for kid in node.children.values():
        if kid.isDirectory:
            listy.append(kid)
            get_all_dirs(listy, kid)


def part1(rootNode):
    dirs = find_all_dirs_less_than(rootNode, 100000)
    total_size = 0
    for dir in dirs:
        print(f"holy crap - dir {dir.name} is of size: {dir.calculatedSize}")
        total_size = total_size + dir.calculatedSize

    print(f"total size is: {total_size}")
    print("yea!  I have a root node.")


def part2(rootNode):
    all_dirs = []
    get_all_dirs(all_dirs, rootNode)

    used_space = rootNode.getSize()
    free_space = 70000000 - used_space
    needed_space = 30000000 - free_space
    deletable_dirs = []
    for dir in all_dirs:
        if dir.calculatedSize >= needed_space:
            deletable_dirs.append(dir)

    deletable_dirs.sort(key=lambda dir:dir.calculatedSize)
    print(f"dir to delete: {deletable_dirs[0].name} of size: {deletable_dirs[0].calculatedSize}")




if __name__ == '__main__':
    rootNode = read_file()
    calc_sizes(rootNode)
    part1(rootNode)
    part2(rootNode)

