ints = [1, 2, 3, 4, 11, 12,111,1234]
# converting elements to string 
temp1 = list(map(str, ints))

# getting max length
max_len = max(map(len, temp1))
print(max_len)
longs = []
for i in temp1:
    if len(i) == max_len:
        longs.append(i)
l=sorted(longs,key=lambda idx:idx[0], reverse=True)
print(longs)
shorts= [idx for idx in temp1 if idx not in longs ]
print(shorts)
max_shorts = max(map(len, shorts))
shor=[]
for idx in shorts:
    shor.append(str(idx).ljust(max_shorts,'a'))
shor.sort(key=lambda x: x[0], reverse=True)
shor.sort(key=lambda x: x[1], reverse=False)
print(f"shor={shor}")
t = []
for idx in ints:
    t.append(str(idx).ljust(max_len, '0'))
print(t)
r = sorted(t, key=lambda idx: idx[0], reverse=True)
res = ''.join(map(str, r))
final = []
for i in res:
    if i.isnumeric():
        final.append(i)

print(''.join(final))
