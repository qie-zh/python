def judge(li:list,n:int):
    for a in range(1,n):
        for b in range(a):
            if mat[a][b] != 0:
                return False
    return True


n = int(input())#矩阵个数

for _ in range(n):
    #获得矩阵
    m = int(input())#矩阵维数
    mat = []
    for j in range(m):
        mat.append(list(map(int,input().split())))
    print('YES' if judge(mat,m) else 'NO')

