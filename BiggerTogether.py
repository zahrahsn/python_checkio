class NumStr(str):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def less_than(self):
        return self.x + self.y < self.y + self.x


def bigger_together(ints):
    # class NumStr(str): __lt__ = lambda x, y: x + y < y + x
    str_ints = list(map(str, ints))
    order = sorted(map( NumStr.less_than, str_ints))
    return int(''.join(reversed(order))) - int(''.join(order))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1, 2, 3, 4]) == 3087, "4321 - 1234"
    # assert bigger_together([1,2,3,4, 11, 12]) == 32099877, "43212111 - 11112234"
    # assert bigger_together([0, 1]) == 9, "10 - 01"
    # assert bigger_together([100]) == 0, "100 - 100"
    # print('Done! I feel like you good enough to click Check')
