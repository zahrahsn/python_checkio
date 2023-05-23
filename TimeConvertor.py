def time_converter(time):
    seprated=time.split(":")
    h=int(seprated[0])
    m=int(seprated[1])
    
    if h>12:
        h=h-12
        mid_or_not="p.m."
    elif h==12:
        mid_or_not="p.m." 
    
    else:
        mid_or_not="a.m."
    return f'{h}:{m:02d} {mid_or_not}'
    
        

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    print(time_converter('09:00'))
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")