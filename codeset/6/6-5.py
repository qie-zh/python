def calculator(x,n):
    count = 0
    for i in x:
        if type(i) == int:
            count += 1*n
        else:
            count += calculator(i,n+1)
    return count
print(calculator(eval(input()),1))