x = int(input())
print('{:.3f}'.format(sum([i/(2*i-1) if i %2 == 1 else -i/(2*i-1) for i in range(1,x+1)] )))