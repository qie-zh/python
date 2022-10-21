num = input().split()
num = [int(i) for i in num]
num.sort()
for i in range(3):
    print(num[i],end = '' if i >= 2 else '->')