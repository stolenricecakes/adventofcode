from monkey import *
from functools import reduce
import re

divido = None

def make_monkies(lines):
   global divido
   monkeyNumRE = re.compile("Monkey (\d+):")
   startingRE = re.compile("Starting items: (.+)$")
   operationRE = re.compile("new = old ([*+]) ([old|\d]+)")
   testRE = re.compile("divisible by (\d+)")
   trueTestRE = re.compile ("true: throw to monkey (\d+)")
   falseTestRE = re.compile ("false: throw to monkey (\d+)")

   monkies = []
   monk = None
   for line in lines:
       line = line.rstrip("\n")
       modifier = 0
       operator = ''
       searchin = monkeyNumRE.search(line)
       startin = startingRE.search(line)
       oper = operationRE.search(line)
       monkTest = testRE.search(line)
       trueTest = trueTestRE.search(line)
       falseTest = falseTestRE.search(line)
       if searchin:
           monk = Monkey()
           monkies.append(monk)
           monk.num = searchin.group(1)
       elif startin:
           nums = startin.group(1).split(", ");
           for num in nums:
               monk.items.append(int(num))
       elif oper:
           operator = oper.group(1)
           modifier = oper.group(2)
           if operator == '+':
               if modifier == 'old':
                   monk.setOper(lambda x: x + x)
               else:
                   monk.setOper(lambda x, m=modifier: x + int(m))
           elif operator == '*':
               if modifier == 'old':
                  monk.setOper(lambda x: x * x)
               else:
                  monk.setOper(lambda x, m=modifier: x * int(m))
           else:
               print(f"what in the buttholes is {operator}?")
       elif monkTest:
           val = int(monkTest.group(1))
           monk.setTesty(lambda x, v=val: x % v == 0)
           monk.setDividoness(lambda x, v=val: v if x % v == 0 else x)
           monk.setDivido(val)
       elif trueTest:
           val = int(trueTest.group(1))
           monk.setTrueTest(lambda v=val: v)
       elif falseTest:
           val = int(falseTest.group(1))
           monk.setFalseTest(lambda v=val: v)

   dividermen = map(lambda x: x.divido, monkies)
   productize = lambda x, y: x * y
   producto = reduce(productize, dividermen)
   divido = lambda y, p=producto: y % p

   return monkies


def take_turns(monkies):
# part2   for round in range(0, 20):
    global divido
    for round in range(0, 10000):
        for monkey in monkies:
            while len(monkey.items) > 0:
                val = monkey.items[0]
                monkey.items = monkey.items[1:]
                monkey.inspectionCount += 1
                val = monkey.oper(val)
                ## part 2 val //= 3
                ##val = monkey.dividoness(val)
                ##val = (val % 96577)
                val = divido(val)
                if monkey.testy(val):
                    nextMonk = monkey.trueTest()
                    monkies[nextMonk].items.append(val)
                else:
                    nextMonk = monkey.falseTest()
                    monkies[nextMonk].items.append(val)
        print(f"round {round} complete")


def do_things():
    monkey = Monkey(0)
    str = "19"
    operation = "%"
    monkey.potty = lambda x: x % int(str) == 0
    if monkey.potty(38):
        print("whee")
    else:
        print("pee")


def read_file():
    f = open("input.txt", "r")
    #f = open("testytesterman.txt", "r")
    lines = f.readlines()
    f.close()
    return lines


def calc_monkey_business(monkies):
    monkies.sort(key=lambda m:m.inspectionCount, reverse=True)
    monkeyval1 = monkies[0].inspectionCount
    monkeyval2 = monkies[1].inspectionCount
    return monkeyval1 * monkeyval2



if __name__ == '__main__':
    lines = read_file()
    monkies = make_monkies(lines)
    take_turns(monkies)
    biznass = calc_monkey_business(monkies)
    print(f"buttpoopies 4 eva ==> {biznass}")
