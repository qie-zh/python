n = int(input())
if n != 0:
    score = list(map(int,input().split()))
    average = float(sum(score)/n)
    count=0
    for i in score:
        if i >= 60:
            count+=1
    print('average = %.1f\ncount = %d'%(average,count))
else:
    print('average = 0.0\ncount = 0')
    exit(0)