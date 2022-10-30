def f(x:int):
    a,b = 1,2
    for i in range(x):
        a,b = b,a+b
    return a

n = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum + f(i)/f(i-1)
print('%.2f'%(sum))