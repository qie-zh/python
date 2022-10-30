n = int(input())
num = list(map(int,input().split()))
max=0
for i in range(len(num)):
    if num[i] > num[max]:
        max = i
print('%d %d'%(num[max],max))
