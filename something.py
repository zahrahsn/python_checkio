def decimaltobinary(res, number):
    if number==0:
        # print('0', end='')
        res.append(0)
    elif number==1:
        # print('1', end='')
        res.append(1)
    else:
        res.append(number % 2)
        decimaltobinary(res, number // 2)
    # print(number % 2, end='')



if __name__ == '__main__':
    # decimal value
    dec_val = 4

    # Calling function
    res = []
    decimaltobinary(res, dec_val)
    return res.count(1)
    str_res = list(map(str, res))
    var=''.join(reversed(str_res))
    count=0
    for i in var:
        if i=='1':
            count+=1
    print(str(count))

