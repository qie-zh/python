def f(a:int):
    if a == 0:
        return 1
    else:
        res = 1
        for i in range(1,a+1):
            res = res*i
        return res
n = int(input())
list = [1/f(i) for i in range(n+1)]
print('%.8f'%(sum(list)))