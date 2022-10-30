str = input()
res = ''
for i in str:
    if 'A' <= i <='Z' and i not in res:
        res = res +i
if res == '':
    print('Not Found')
else:
    print(res)