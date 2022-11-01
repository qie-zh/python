coin = int(input())
count = 0
for fen5 in range(coin//5+1,0,-1):
    for fen2 in range(coin//2+1,0,-1):
            fen1 = coin - fen5*5 - fen2*2
            if fen1 >0:
                print('fen5:%d, fen2:%d, fen1:%d, total:%d'%(fen5,fen2,fen1,fen5+fen2+fen1))
                count+=1
print('count = %d'%(count))