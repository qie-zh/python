str = input()
flag = -1
n = len(str)
print(str)
for i in range(n//2):
    if str[i] != str[n-1-i]:
        flag = 1
        print('No')
        break
if flag != 1:
    print('Yes')

