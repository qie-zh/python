m = eval(input())
n = eval(input())

#融合两个字典
for i in m.keys():
    n[i] = n.get(i,0) + m.get(i)

#把字典字符翻译成整型
record = {}    #键是翻译过的原字典键，键值是未翻译的原字典键
for i in n:
    if type(i) == str:
        record[ord(i)] = record.get(ord(i),i)
    else:
        record[i] = record.get(i,i)

record_keys = sorted(list(record.keys()))
print('{',end = '')
for i in record_keys:
    if type(record[i]) == str:
        print('"%s":%d'%(record[i],n[record[i]]),end='')
    else:
        print('%d:%d'%(record[i],n[record[i]]),end='')
    print(',' if i != record_keys[-1] else '}',end='')