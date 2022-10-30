from ctypes.wintypes import tagRECT


str = input().strip()
target = input().strip()
str = str.replace(target.upper(),'')
str = str.replace(target.lower(),'')

print('result: %s'%(str))