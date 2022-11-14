list = list(map(int,input().split()))
max,sum = 0,0
for i in range(1,4):
    for j in range((i-1)*3,i*3):
        print('%4d'%(list[j]),end='')
        sum += list[j]
        if list[j] > max:
            max = list[j]
    print('%4d%4d'%(max,sum))
    max,sum = 0,0

