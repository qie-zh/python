str = input()
s = '0123456789abcdefABCDEF'
result = ''
flag = 1
for i in str:
    if i in s:
        result = result+i
    if i == '-' and flag == 1:
        flag = -1
print(result)
print(0 if len(result) == 0 else int(result,16)*flag)