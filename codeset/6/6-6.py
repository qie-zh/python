def calculator(x,m,count):
    if m == 1:
        for i in x:
            if type(i) == int:
                count+=1
    for i in x:
        if type(i) == list:
            count = calculator(i,m-1,count)
    return count

li = eval(input())
n = int(input())

print(calculator(li,n,0))
