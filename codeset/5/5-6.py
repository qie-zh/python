n = int(input())
age = map(int,input().split())

dic = {}
for i in age:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
for i in range(51):
    if i in dic:
        print('%d:%d'%(i,dic[i]))