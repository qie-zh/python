a = input()
str = input()
flag = -1
for i in range(len(str)):
    if str[i] == a:
        flag = i
if flag < 0:
    print('Not Found')
else:
    print('index = %d'%(flag))