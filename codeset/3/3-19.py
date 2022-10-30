n = int(input())
s = ''
for i in range(n):
    str = input()
    if len(str) > len(s):
        s = str
print('The longest is: %s'%(s))
