def divisors(n):
    divisers = []
    for i in range(1, n + 1):
        if (n % i) == 0:
            divisers.append(i)
    return divisers


def greatest_common_divisor(*args: int) -> int:
    nums = set(args)
    mydict = {}
    for i in nums:
        div = divisors(i)
        mydict[i] = div

    lis = list(mydict.values())
    lis.sort(key=len)
    common = {}
    for i in lis[0]:
        common[i]=0
        for j in  range(1,len(lis)):
            if i in lis[j]:
                common[i]+=1
    max_keys = [key for key, value in common.items() if value == max(common.values())]
    maxkey= [int(ma) for ma in max_keys]
    return max(maxkey)



if __name__ == "__main__":
    print("Example:")
    # print(greatest_common_divisor(6, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert greatest_common_divisor(6, 4) == 2
    # assert greatest_common_divisor(2, 4, 8) == 2
    # assert greatest_common_divisor(2, 3, 5, 7, 11) == 1
    # assert greatest_common_divisor(3, 9, 3, 9) == 3
    assert greatest_common_divisor(4294967296, 2) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
