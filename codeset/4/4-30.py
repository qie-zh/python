import math
def factor(a:list,b:int):
    for i in range(2,int(math.sqrt(b)+1)):
        if b % i == 0:
            a.append(i)
            if b//i != i:
                a.append(b//i)
    if sum(a) == b:
        return True
    else:
        return False
m,n = map(int,input().split())
flag = 0
for i in range(m,n+1):
    res = [1]
    if factor(res,i):
        flag = 1
        print('%d = '%(i),end = '')
        res.sort()
        for j in range(len(res)):
            print('%d'%(res[j]),end = ' + ' if j < len(res)-1 else '\n')

if flag == 0:
    print('None')