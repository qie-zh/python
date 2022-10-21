a,b = map(int,input().split())
for i in range(a,b+1):
    print('{0:>5}'.format(i),end='\n' if (i-a+1) % 5 ==0 else '')
print('\n' if (i-a+1)%5!=0 else '',end='')
print('sum =',sum(i for i in range(a,b+1)))