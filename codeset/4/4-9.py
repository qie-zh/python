fruit = {'apple':3.00,'pear':2.50,'orange':4.10,'grape':10.20}
fruit_key = list(fruit.keys())
fruit_key.append('exit')
for i in range(5):
    print('[%d] %s'%(i+1 if i != 4 else 0,fruit_key[i]))
input = list(map(int,input().split()))
for i in range(5):
    n = input[i]
    if n == 0:
        break
    else:
        print('price = %.2f'%(fruit[fruit_key[n-1]]))