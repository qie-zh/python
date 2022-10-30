str = input()
count = 0
result = ''
for i in str:
    if 'a' <= i <= 'z' or 'A' <= i <='Z':
        if i.upper() not in result and i.lower() not in result:
            count+=1
            result = result + i
    if count == 10:
        print(result)
        break
if count < 10:
    print('not found')


