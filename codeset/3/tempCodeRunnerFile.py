n = int(input())
num = list(map(int,input().split()))
max=0
min=0
for i in range(len(num)):
    if num[i] > num[max]:
        max = i
    if num[i] < num[min]:
        min = i

print('%d %d'%(max,min))
