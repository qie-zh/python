from unittest.util import sorted_list_difference


s = input()
res = ''
for i in s:
    if 'A' <= i <='Z':
        res = res + chr(ord('A')+ord('Z')-ord(i))
    else:
        res = res + i

print(res)