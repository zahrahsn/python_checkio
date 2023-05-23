import string


def from_camel_case(name: str) -> str:
    res = []
    for k,i in enumerate(name):
        if i not in string.ascii_lowercase:
            if k==0:
                res.append(i.lower())
            else:
                res.append("_"+i.lower())
        else:
            res.append(i)
    return "".join(res)

if __name__ == '__main__':
    print("Example:")
    print(from_camel_case("Name"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case("ThisFunctionIsEmpty") == "this_function_is_empty"
    assert from_camel_case("Name") == "name"
    print("Coding complete? Click 'Check' to earn cool rewards!")