
from typing import List
def tidy(w):
    consonant=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    vowel=['a','e','i','o','u','y']
    res=[]
    q=[]
    i = 0
    while i < len(w):
        if w[i] in consonant:
            res.append(w[i])
            i +=2
        else:
            res.append(w[i])
            i+=3

    return ''.join(res)



def translate(text: str) -> str:
    words = text.split()
    tidy_result=[]
    for w in words:
        tidy_result.append(tidy(w))
    return ' '.join(tidy_result)


if __name__ == "__main__":
    print("Example:")
    print(translate("hieeelalaooo"))
    # print(translate("sooooso aaaaaaaaa"))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
