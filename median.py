from typing import List


def recogniser(data: List[int]) -> [int, float]:
    if len(data) % 2 == 0:
        m_index1 = (len(data) // 2 ) -1
        m_index2 = len(data) // 2
        data.sort()
        medianvalues = data[m_index1], data[m_index2]
        return (medianvalues[0] + medianvalues[1]) / 2
    else:
        m_index = len(data) // 2
        data.sort()
        return data[m_index]


def checkio(data: List[int]) -> [int, float]:
    return recogniser(data)


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")
