def factor(a:int):
    factor = []
    for i in range(1,a+1):
        if a % i == 0:
            factor.append(i)
    return factor

m,n = map(int,input().split())
m_list=factor(m)
n_list=factor(n)
com_factor = 0

for i in m_list:
    if i in n_list:
        com_factor = i

print('%d %d'%(com_factor,n*m/com_factor))