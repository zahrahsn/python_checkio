first=0
n=9
fib=[]
for i in range(0,n):
    if i==0 or i ==1:
        fib.append(i)
    
        
        
    else:
        fib.append(fib[i-1]+fib[i-2])
        
print(fib)            
    
    