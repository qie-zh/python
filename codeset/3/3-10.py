str = input()
signs = 'BCDFGHJKLMNPQRSTVWXYZ'
count=0
for i in str:
    if i in signs:
        count+=1

print(count)