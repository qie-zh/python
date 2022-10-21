l,u = map(int,input().split())
if l > u :
    print('Invalid.')
else:
    print('fahr celsius')
    for i in range(l,u+1,2):
        print('{:.0f}{:6.1f}'.format(i,5*(i-32)/9))