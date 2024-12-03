
def read_crap():
#    f = open("sample.txt", "r")
    f = open("datas.txt", "r")
    lines = f.readlines()
    reports = []
    for line in lines:
        report = []
        for str in line.rstrip("\n").split(" "):
           report.append(int(str))
        reports.append(report)
    f.close()
    return reports



def is_safe(val1, val2, increasing):
    return val1 != val2 and (abs(val1-val2) <= 3) and ((val1 < val2 and increasing) or (val1 > val2 and not increasing))


def is_report_safe(report):
    val1 = report[0]
    val2 = report[1]
    increasing = val1 < val2
    safe = True
    for i in range(0, len(report) - 1):
        safe = safe and is_safe(report[i], report[i + 1], increasing)
    return safe


def count_part1_safes(reports):
    safes = 0
    for report in reports:
        if is_report_safe(report):
            safes += 1

    return safes


def count_part2_safes(reports):
   safes = 0
   for report in reports:
       if is_report_safe(report):
           safes += 1
       else:
# see if dropping values makes safeness.
           for i in range(0, len(report)):
               new_report = report.copy()
               del new_report[i]
               if is_report_safe(new_report):
                   safes += 1
                   break
   return safes



if __name__ == '__main__':
    reports = read_crap()
    num_safes = count_part1_safes(reports)
    print(f"holy dingles, there are {num_safes} safe reports")
    part2_safes = count_part2_safes(reports)
    print(f"wowzo ding dong, there's {part2_safes} safe after dropping crap")


# 533 is too low. hmmmmmm...