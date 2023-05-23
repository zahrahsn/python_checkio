# def p(*args,**kwargs):
#     print(args)
#     print(kwargs)

# p(1,2,3,oper="hello",op="bye")

# from email import message


# def k(num1,num2,operation='sum'):
#     print(locals())
#     print(globals())
# k(4,5,'multiply')


# def function1(varA,varB):
#     message="some local data"
#     print(varA)
#     def inner_function(varA,varB):
#         print(f'inner_function local scope:{locals()}')
#     print(locals())
#     inner_function(123,456)
# function1(1,2)


# class Dog:
#     _legs = 4
    
#     def __init__(self, name):
#         self.name = name
        
#     def getLegs():
#         return Dog._legs  
    
#     def speak(self):
#         print(self.name +"says:Bark")    
        
        
# mydog=Dog('kooni')        
# print(mydog.name)
# print(Dog._legs)
# print(mydog.getLegs())


# Dog._legs=3
# mydog=Dog('kooni')        
# print(mydog.name)
# print(Dog._legs)
# print(mydog.getLegs())



# class UniqueList(list):
#     def append(self,item):
#         if item in self:
#             return 
#         super().append(item)
        
# uniquelist=UniqueList()
# uniquelist.append(1)
# uniquelist.append(1)        
# uniquelist.append(2)
# print(uniquelist)        
 
 
 
 
# from multiprocess import Process  
# import time
# import threading
# if __name__ ==  '__main__':
#     def longSquare(num,results):
#         time.sleep(1)
#         # print(num**2)
#         # print('finished computing!')
#         results[num]=num**2
        
#     # results={}
#     # process=[Process(target=longSquare, args=(n,results)) for n in range(0,10)]         

#     # [p.start() for p in process]
#     # [p.join() for p in process]
        
    
#     resu={}
#     threads=[threading.Thread(target=longSquare,args=(n,resu)) for n in range(0,10)]
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
#     print (resu)
    