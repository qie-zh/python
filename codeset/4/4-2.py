import math
m,n = map(int,input().split())
sum = count = flag = 0
for i in range(m,n+1):
    if i == 1:
        continue
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        sum = sum + i
        count+=1
    else:
        flag = 0
print('%d %d'%(count,sum))