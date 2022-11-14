point = int(input())
edge = 0
length = 0
for _ in range(point):
    s = input()
    dic = eval(s)
    for i in dic:
        edge += len(dic[i])
        for j in dic[i]:
            length += dic[i][j]
    
print('%d %d %d'%(point,edge,length))