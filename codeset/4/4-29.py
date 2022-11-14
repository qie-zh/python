m = list(map(int,input().split()))[1:]
n = list(map(int,input().split()))[1:]
sam = []
res = []
for i in m:
    if i in n:
        sam.append(i)
m.extend(n)
for i in m:
    if i not in sam and i not in res:
        res.append(i)

for i in range(len(res)):
    print(res[i],end='' if i ==len(res)-1 else ' ')