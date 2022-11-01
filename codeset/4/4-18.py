n = int(input())
line = [i for i in range(1,n+1)]

k,i = 1,0
while len(line) > 1:
    if k == 3:
        k = 1
        line.pop(i)
    else:
        k +=1
        i = (i+1)%len(line)

print(line[0])
