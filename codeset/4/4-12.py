def fib(x:int):
    a,b = 0,1
    while a < x:
        a,b = b,a+b
    return a

print(fib(int(input())))