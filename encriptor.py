# import string
# def to_encrypt(text, delta):
#     result = ""
#     alphabets = list(string.ascii_lowercase)
#     for i in text:
#         if i == ' ':
#             result += i
#         else:
#             for k, v in enumerate(alphabets):
#                 if i == v:
#                     dif = k + delta
#                     if dif >= len(alphabets):
#                         r = alphabets[abs(len(alphabets) - dif)]
#                     else:
#                         r = alphabets[dif]
#                     result += r
#
#     return result
#
#
# if __name__ == '__main__':
#     print("Example:")
#     print(to_encrypt('abc', 10))
#
#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert to_encrypt("a b c", 3) == "d e f"
#     assert to_encrypt("a b c", -3) == "x y z"
#     assert to_encrypt("simple text", 16) == "iycfbu junj"
#     assert to_encrypt("important text", 10) == "swzybdkxd dohd"
#     assert to_encrypt("state secret", -13) == "fgngr frperg"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Goes Right After
import array
import re
def goes_after(word: str, first: str, second: str) -> bool:
    first_one = [i.start() for i in re.finditer(first, word)]
    second_one = [i.start() for i in re.finditer(second, word)]
    if len(first_one)==0 or len(second_one) == 0:
        return False
    return first_one[0] == second_one[0]-1


if __name__ == "__main__":
    print("Example:")
    print(goes_after("world", "w", "o"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after("world", "w", "o") == True
    assert goes_after("world", "w", "r") == False
    assert goes_after("world", "l", "o") == False
    assert goes_after("panorama", "a", "n") == True
    assert goes_after("list", "l", "o") == False
    assert goes_after("", "l", "o") == False
    assert goes_after("list", "l", "l") == False
    assert goes_after("world", "d", "w") == False
    assert goes_after("transport", "r", "t") == False
    print("Coding complete? Click 'Check' to earn cool rewards!")