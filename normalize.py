import sys
import string


def max(list):
    max = list[0]
    for item in list:
        if item > max:
            max = item

    return max


def round(f):
    if int(f + 1) - f < f - int(f):
        return int(f + 1)
    else:
        return int(f)


results = []
for line in sys.stdin:
    # print(line, end="")
    list = [float(x.strip()) for x in line.split(',')]
    # print(list)
    M = max(list)
    # print(M)
    # d = 100/M
    new = [round(i * 100 / M) for i in list]
    # print(new)
    results.append(new)

for list in results:
    sep = ','
    str_list = [str(x) for x in list]
    print(sep.join(str_list))
    # print()
