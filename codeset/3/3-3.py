str = input()
char1,char2 = input().split()
for i in range(len(str)-1,-1,-1):
    if str[i] == char2:
        print('%d %c'%(i,char2))
    if str[i] == char1:
        print('%d %c'%(i,char1))