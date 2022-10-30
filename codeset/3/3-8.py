str = input()
str_list = []
for i in range(len(str)-1,-1,-1):
    str_list.append(str[i])

print(''.join(str_list))