m = list(input().split(','))
team2 = {'6':0,'7':0,'8':0,'9':0,'10':0}
flag = 1
for i in m:
    if i in team2:
        team2[i] += 1

for i in team2:
    if team2[i] == 0:
        if flag :
            print(i,end='')
            flag = 0
        else:
            print(' %s'%(i),end='')