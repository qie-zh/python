str = list(input())
for i in range(len(str)):
    for j in range(len(str)-1-i):
        if str[j] > str[j+1]:
            str[j],str[j+1] = str[j+1],str[j]
res = ''
for i in str:
    if i not in res:
        res = res + i

print(res)