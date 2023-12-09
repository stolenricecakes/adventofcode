
def read_in_file():
    f = open("input.txt", "r")
    line = f.readline()
    f.close()
    return line

def find_first_non_repeat(stuff, largeness):
    idx = 0
    stuff_list = list(stuff)
    print(f"looking for pattern in {len(stuff_list)} chars ")
    myset = set(stuff_list[idx:largeness])
    while len(myset) < largeness:
        idx = idx + 1
        print(f"{myset}")
        myset = set(stuff_list[idx:largeness + idx])


    print(f"holy tinkles, idx is: {idx} and chars are: {stuff_list[idx:idx + largeness]}")
    print(f"answer is {idx + largeness}")



if __name__ == '__main__':
    stuff = read_in_file()
    ## part 1:
    #find_first_non_repeat(stuff, 4)
    ## part 2
    find_first_non_repeat(stuff, 14)
    print("all done")