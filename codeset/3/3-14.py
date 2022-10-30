str = input()[:-1]
res = ''
for i in str:
    if 'A' <= i <= 'Z':
        res = res + chr(ord(i)+32)
    elif 'a' <= i <= 'z':
        res = res + chr(ord(i)-32)
    else:
        res = res + i

print(res)