import math
def isPrime(a:int):
    if a == 1:
        return False
    else:
        for i in range(2,int(math.sqrt(a))+1):
            if a % i == 0:
                return False
    return True

num = int(input())
for i in range(num//2+1):
    if isPrime(i) and isPrime(num-i):
        print('%d = %d + %d'%(num,i,num-i))
        break

