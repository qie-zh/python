def fib(x:int):
    a,b = 0,1
    for i in range(x):
        a,b = b,b+a
    return a

n = int(input())
list = [fib(i) for i in range(1,n+1)]
count = 0
if n <1:
    print('Invalid.')
else:
    for i in list:
        print('%11d'%(i),end='')
        count+=1
        if count %5 == 0:
            print()
    if count%5 != 0:
        print()