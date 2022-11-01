n = int(input())
mat = []
for i in range(n):
    mat.append(list(map(int,input().split())))
sum = 0
for i in range(n-1):
    for j in range(n-1):
        if i != n-j-1:
            sum += mat[i][j]
print(sum)