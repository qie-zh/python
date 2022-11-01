import math
def isprime(a:int):
    if a == 1:
        return False
    for i in range(2,int(math.sqrt(a))+1):
        if a % i ==0:
            return False
    return True

n = int(input())
for _ in range(n):
    a = int(input())
    print('Yes' if isprime(a) else 'No')
