err = float(input())
def fact(a:int):
    res = 1
    for i in range(1,a):
        res *= i
    return 1.0/res
n,res = 1,0
while fact(n) > err:
    res += fact(n)
    n +=1

print('%.6f'%(res+fact(n)))