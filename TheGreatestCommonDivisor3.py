def div(sorting):
    newlist = []
    for i in range(len(sorting) - 1):
        newlist.append(divising(sorting[i], sorting[i + 1]))
    return newlist


def divising(i, j):
    if i % j == 0:
        return j
    else:
        maghsum = i
        maghsumelayh = j
        remnent = maghsum % maghsumelayh
        while remnent != 0:
            maghsum = maghsumelayh
            maghsumelayh = remnent
            remnent = maghsum % maghsumelayh
        return maghsumelayh


def greatest_common_divisor(*args: int) -> int:
    if len(set(args)) == 1:
        nums = args
    else:
        nums = list(set(args))
    sorting = sorted(nums, reverse=True)
    newlist = div(sorting)

    if len(set(newlist)) == 1:
        return newlist[0]
    else:

        lo = div(newlist)
        l=len(set(lo))
        while l != 1:

            lo=div(lo)
            l = len(set(lo))
    return lo[0]


if __name__ == "__main__":
    print("Example:")
    print(greatest_common_divisor(6, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert greatest_common_divisor(6, 4) == 2
    assert greatest_common_divisor(2, 4, 8) == 2
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1
    assert greatest_common_divisor(3, 9, 3, 9) == 3
    assert greatest_common_divisor(4294967296, 2) == 2
    assert greatest_common_divisor(1, 1) == 1
    assert greatest_common_divisor(4294967296, 1610612736)
    assert greatest_common_divisor(32, 256, 2048, 16384, 131072, 1048576, 8388608, 67108864, 536870912,
                                   4294967296) == 32
