ints = [3,12,22,32]
temp1 = list(map(str, ints))
max_len = max(map(len, temp1))
print(max_len)
# k=[x.ljust(max_len,'0') for x in temp1]
ints.sort(key=lambda x:str(x).ljust(max_len,'0'), reverse=True)
ints_str = list(map(str, ints))
max_num = int(''.join(ints_str))
print(max_num)
min_num=int(''.join(reversed(ints_str)))
print(min_num)
result= max_num - min_num
print(result)
# for i in range(0, max_len):
#     so = sorted([f for f in temp1 if len(f) == i + 1], key=lambda x: x[i], reverse=True)
#     print(f"So={so}")
