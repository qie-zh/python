str = input().split()

for i in range(len(str)):
    for j in range(len(str)-1-i):
        if str[j] > str[j+1]:
            str[j],str[j+1] = str[j+1],str[j]
print('After sorted:')
for i in str:
    print(i)