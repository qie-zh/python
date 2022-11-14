n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))


max_i,max_j = 0,0
for i in range(n):
    for j in range(n):
        if mat[i][j] > mat[max_i][max_j]:
            max_i = i
            max_j = j
        for a in range(n):
            if mat[max_i][max_j] > mat[max_i][a]

    print('i = %d,j = %d'%(max_i,max_j))
