nums = input()
sum = count = 0
for i in nums:
    sum = sum + int(i)
    count+=1
print('%d %d'%(count,sum))