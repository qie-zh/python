m = int(input())
mark = input()
n = int(input())
flag = 0
try:
    dic = {'+':m+n,'-':m-n,'*':m*n,'/':m/n}
except ZeroDivisionError:
    print('divided by zero')
    flag = 1

if not flag:
    print('%.2f'%(dic[mark]))
    '''
    if dic[mark] == int(dic[mark]) :
        print('%d'%(dic[mark]))
    else:
        print('%.2f'%(dic[mark]))'''