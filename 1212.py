_8num = list(map(int, input()))
tmp = ''    
res = ''
print(_8num)
for n in _8num:
    while n > 0:
        tmp+=str(n % 2)
        n = n // 2
    if len(tmp) < 3:
        tmp[::-1]
        res += tmp.zfill(3)
        tmp = ''
    else:
        tmp[::-1]
        res +=tmp
print(tmp)