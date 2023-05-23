ints = [1, 2, 3, 4, 11, 12, 111, 1234]
import itertools


def sort_by(t):
    return range(0, t)


ints = [32, 22, 12, 3]
temp1 = list(map(str, ints))
max_len = max(map(len, temp1))
# print(max_len)
li = []
for i in range(0, max_len):
    so = sorted([f for f in temp1 if len(f) == i + 1], key=lambda x: x[0:i + 1], reverse=True)
    li.append(so)
    for x in li:
        if len(x) == 0:
            li.remove(x)
    # print(li)
    # print(len(li))
    # while len(li) != 1:
for i in range(1, len(li)):
    for x in li[i]:
        t = len(x)
        for j in li[0]:
            li[0].append(x)
            li[0] = sorted(li[0], key=lambda y: (str(y).ljust(max_len, '0')[0], str(y).ljust(max_len, '0')[1]), reverse=True)

print(li[0])

#
# max_num = int(''.join(li[0]))
# print(max_num)
# min_num = int(''.join(reversed(li[0])))
# print(min_num)
# result = max_num - min_num
# print(result)
