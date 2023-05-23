def divisors(n):
    divisers = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            divisers.append(i)
    return divisers


def greatest_common_divisor(*args: int) -> int:
    nums = list(set(args))
    sorting = sorted(nums)
    if len(sorting) == 2:
        if sorting[1] % sorting[0] == 0:
            return sorting[0]
        else:
            maghsum = sorting[1]
            maghsumelayh = sorting[0]
            remnent = maghsum % maghsumelayh
            while remnent != 0:
                maghsum = maghsumelayh
                maghsumelayh = remnent
                remnent = maghsum % maghsumelayh
            return maghsumelayh
    little = sorting[0]
    remain = sorting[1:]
    divs = divisors(little)
    mydict = {}
    for i in divs:
        mydict[i] = 0
        for j in remain:
            if j % i == 0:
                mydict[i] += 1
    max_keys = [key for key, value in mydict.items() if value == len(remain)]
    maxkey = [int(ma) for ma in max_keys]
    return max(maxkey)


if __name__ == "__main__":
    print("Example:")
    print(greatest_common_divisor(6, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert greatest_common_divisor(6, 4) == 2
    assert greatest_common_divisor(2, 4, 8) == 2
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1
    assert greatest_common_divisor(3, 9, 3, 9) == 3
    assert greatest_common_divisor(4294967296, 2) == 2
    # assert greatest_common_divisor(4294967296, 1610612736)
