import math
n = int(input())

for i in range(int(math.pow(10,n-1)),int(math.pow(10,n))):
    a,sum = i,0
    while a > 0:
        sum = sum + pow(a%10,n)
        a = a//10
    if sum == i:
        print(i)
        continue