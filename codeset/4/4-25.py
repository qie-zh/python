n = int(input())
alpha = 65

while n > 0:
    for i in range(n):
        print('%c '%(chr(alpha)),end='')
        alpha+=1
    n-=1
    print()
