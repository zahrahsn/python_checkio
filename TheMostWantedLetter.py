def checkio(text: str) -> str:
    li = []
    fi = []
    listing = list(text)
    for i in listing:
        if i.isalpha():
            li.append(i.lower())
    dic = {i: li.count(i) for i in li}
    if len(set(dic.values())) == 1:
        fi.extend(dic.keys())
        fi.sort()
    else:
        keys = list(dic.keys())
        keys.sort()
        s = sorted(keys, key=lambda x: dic[x], reverse=True)
        fi.append(s[0])
    return fi[0]


if __name__ == '__main__':
    print("Example:")
    # print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Lorem ipsum dolor sit amet") == 'm'
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
