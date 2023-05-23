# a = [1,1,1,2,2,3,3,3,3]
# m = max(a, key=a.count)
# print(m) 
# x=int(a) for a in str(number)
# max(x)
# def correct_sentence(text: str) -> str:
#     if len(text) > 1 and text[-1] != ".":
#         text = text + "."
#
#     return text[0].capitalize()

# def split_pairs(a):
#     if len(a) % 2 !=0:
#        a= a+'_'
#     l=[]
#
#     while len(a)>0:
#         length=len(a)
#         sliced = a[0:2]
#         a = a[2:]
#
#
#         l.append(sliced)
#     return l


# def beginning_zeros(number: str) -> int:
#     if number[0] != '0':
#         return 0
#     else:
#         l = []
#         v = 0
#         while v < len(number) and number[v] == '0':
#             l.append(v)
#             v += 1
#         return len(l)
#
# def nearest_value(values: set, one: int) -> int:
#     if one in values:
#         return one
#     else:
#         values.add(one)
#         sorted_value = sorted(values)
#         if one!= sorted_value[0] and one != sorted_value[-1]:
#             before = 0
#             after = 0
#             for k, v in enumerate(sorted_value):
#                 if v == one:
#                     before = sorted_value[k - 1]
#                     after = sorted_value[k + 1]
#                     r_before = before - v
#                     r_after = after - v
#                     if abs(r_before) < abs(r_after) or abs(r_before) == abs(r_after) :
#                         return before
#                     else:
#                         return after
#         elif one == sorted_value[0]:
#             return sorted_value[1]
#         else:
#             return sorted_value[-2]

# from typing import List
#
# def bigger_together(ints: List[int]) -> int:
#     import itertools
#     ints = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     possibilities = []
#     all_combs = itertools.permutations(ints)
#     for c in all_combs:
#         if c[0] != 0:
#             possibilities.append(
#                 int(''.join(map(str, c)))
#             )
#     maxx = max(possibilities)
#     minn = min(possibilities)
#     diff = maxx - minn
#     print(maxx)
#     print(minn)
#     return diff
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert bigger_together([1,2,3,4]) == 3087, "4321 - 1234"
#     assert bigger_together([1,2,3,4, 11, 12]) == 32099877, "43212111 - 11112234"
#     assert bigger_together([0, 1]) == 9, "10 - 01"
#     assert bigger_together([100]) == 0, "100 - 100"
#     print('Done! I feel like you good enough to click Check')
def decimaltobinary(number):
    storages=[]
    if number > 1 :
        result = number //2
        store= number % 2
        storages.append(store)
        decimaltobinary(result)
    return storages


def checkio(number: int) -> int:
    storages=decimaltobinary(number)
    return 1


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
