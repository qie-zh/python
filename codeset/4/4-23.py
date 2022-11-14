m,n = map(int,input().split())
mat = []
flag = 0
for _ in range(m):
    mat.append(list(map(int,input().split())))

for i in range(1,m-1):
    for j in range(1,n-1):
        if mat[i][j] > mat[i][j-1] and mat[i][j] > mat[i][j+1] and mat[i][j] > mat[i-1][j] and mat[i][j] > mat[i+1][j]:
            print('%d %d %d'%(mat[i][j],i+1,j+1))
            flag = 1
if flag == 0:
    print('None %d %d'%(m,n))