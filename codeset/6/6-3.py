def calculator(x):
    sum = 0
    for i in x:
        if type(i) == int:
            sum += i
        elif type(i) == tuple or type(i) == list:
            sum += calculator(i)
    return sum
print(calculator(list(eval(input()))))
