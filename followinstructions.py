from typing import Tuple


def nav(pos: list, idx, val):
    pos[idx] += val


def follow(instructions: str) -> Tuple[int, int]:
    pos = [0, 0]

    func = {
        'f': lambda x: nav(x, 1, 1),
        'b': lambda x: nav(x, 1, -1),
        'l': lambda x: nav(x, 0, -1),
        'r': lambda x: nav(x, 0, 1)
    }

    for i in instructions:
        func[i](pos)

    return tuple(pos)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
