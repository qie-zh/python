def calculator(x,n):
    sum = 0
    for i in x:
        if type(i) == int:
            sum += i*n
        else:
            sum += calculator(i,n+1)
    return sum
print(calculator(eval(input()),1))