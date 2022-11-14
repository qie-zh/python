n = int(input())
boys = []
girls = []
order_sex = []
for _ in range(n):
    sex,name = input().split()
    order_sex.append(sex)
    if sex == '0':
        girls.append(name)
    else:
        boys.append(name)
for i in range(n//2):
    if order_sex[i] == '0':
        print("%s %s"%(girls.pop(0),boys.pop()))
    else:
        print("%s %s"%(boys.pop(0),girls.pop()))