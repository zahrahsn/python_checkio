# ints = [32, 22, 12, 3]
ints = [4, 3, 2, 1, 11, 12]
temp1 = list(map(str, ints))
max_len = max(map(len, temp1))
ints_just = list(map(lambda x: str(x).ljust(max_len, "a"), temp1))

so = sorted(ints_just, key=lambda x: (x[0], x[1]), reverse=True)
print(so)

joint = ''.join(so)
joint_filtered = list(filter(lambda x: x.isnumeric(), joint))
print(int(''.join(joint_filtered)))
