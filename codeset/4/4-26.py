n = int(input())
sum,tem = 0,1
for i in range(1,n+1,2):
    for j in range(1,i+1):
        tem *= j
    sum += tem
    tem = 1
print('n=%d,s=%d'%(n,sum))