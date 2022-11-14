li = list(map(int,input().split(',')))
n = int(input())
dic = {}

for i in li:
    dic[i] = dic.get(i,n-i)
flag = 0
for i in range(len(li)):
    if li[i] in dic.values():
        if not flag:
            print(i,end='')
            flag+=1
        else:
            print(' %d'%(i),end='')
if not flag:
    print('no answer')