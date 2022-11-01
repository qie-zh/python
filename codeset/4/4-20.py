m,n = map(int,input().split())
n = []
for i in range(m):
    n.append(list(map(int,input().split())))

for i in n:
    print(sum(i))