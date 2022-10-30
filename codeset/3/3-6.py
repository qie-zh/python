num = list(map(int,input().split()))
n = num.pop(0)
res_count=[]
for i in num:
    count = 0
    for j in num:
        if i == j:
            count+=1
    res_count.append(count)

max_count = -1
for i in range(len(res_count)):
    if(res_count[i] > max_count):
        max_count = res_count[i]
        res_num = num[i]
print('%d %d'%(res_num,max_count))