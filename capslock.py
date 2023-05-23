def caps_lock(text: str) -> str:
    result=[]
    a_counter=0
    for v in text:
        if v=='a':
            a_counter+=1
            continue
        else:
            if v.isupper():
                result.append(v)
            elif a_counter%2!=0:
                result.append(v.upper())
            else:
                result.append(v.lower())
    return ''.join(result)


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))
    print(caps_lock("Always wanted to visit Zambia."))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
