c = float(input())
print('Invalid Value!' if c < 0 else 'cost = {:.2f}'.format(c*0.53 if c < 50 else 50*0.53+0.58*(c-50)))