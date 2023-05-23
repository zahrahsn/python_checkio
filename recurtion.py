# def factorial(num):
#     if num==1:
#         return 1
#     else:
#        return  num * factorial(num-1)
#
#
# if __name__== '__main__':
#     decval=3
#     x=factorial(decval)
#     print(x)


def counter(number):
    if number==0:
        print('0')

    else:
        print(str(number))
        counter(number-1)

if __name__== '__main__':
    counter(5)

