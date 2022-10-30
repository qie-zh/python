str = input()
str_list = list(str)
num = 0

for i in str_list:
    if i >='0' and i <='9':
        num = num*10+int(i)

print(num)
