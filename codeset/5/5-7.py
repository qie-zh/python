li = eval(input())
dic = {}
for i in li:
    if i not in dic:
        dic[i] = 1
flag = 0
'''
for i in dic:
    if flag:
        print(' %d'%(i),end='')
    else:
        print(i,end='')
        flag = 1'''
print(' '.join('%s'%k for k in dic))