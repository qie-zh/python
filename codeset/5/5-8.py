m,n = map(int,input().split())
se = set(i for i in range(m,n+1) if i%3 == i%5 == i%7 == 0 )
print(len(se))