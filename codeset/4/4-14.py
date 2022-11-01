count,letter,blank,digit,other = 0,0,0,0,0
li = []
while True:
    s = list(input())
    li.extend(s)
    count+=1
    if count+len(li) > 10:
        break
for i in li:
    if i.isalpha():
        letter+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        blank+=1
    else:
        other+=1
print('letter = %d, blank = %d, digit = %d, other = %d'%(letter,blank+count-1,digit,other))