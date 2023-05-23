import re
import string
def to_decrypt(cryptotext, delta):
    result = ""
    regex = r"[^a-zA-Z\s]*"
    s = re.sub(regex, '', cryptotext)
    alphabets = list(string.ascii_lowercase)
    for i in s:
        if i == ' ':
            result += i
        else:
            for k, v in enumerate(alphabets):
                if i == v:
                    if k + delta >= len(alphabets):
                        idx = k + delta - len(alphabets)
                        r = alphabets[idx]
                    else:
                        r = alphabets[k + delta]
                    result += r
    return result


if __name__ == '__main__':
    # print("Example:")
    # print(to_decrypt('abc', 10))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_decrypt("!d! [e] &f*", -3) == "a b c"
    assert to_decrypt("x^$# y&*( (z):-)", 3) == "a b c"
    assert to_decrypt("iycfbu!@# junj%&", -16) == "simple text"
    print(to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10))
    print(to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10))
    assert to_decrypt("*$#%swzybdkxd !)(^#%dohd", -10) == "important text"
    assert to_decrypt("fgngr **&&frperg^__^", 13) == "state secret"
    print("Coding complete? Click 'Check' to earn cool rewards!")
