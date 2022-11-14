str = list(input())
ch = input()
alpha = {}
for i in str:
    if i not in alpha:
        alpha[i] = 1
    else:
        alpha[i] +=1

if ch in alpha:
    print(alpha[ch])
else:
    print(0)