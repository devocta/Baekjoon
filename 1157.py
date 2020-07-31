str=list(input().upper())
tmp={}
for s in str:
    if tmp.get(s):
        tmp[s]+=1
    else:
        tmp[s] = 1
stmp = dict(sorted(tmp.items(), key = lambda x:x[1], reverse=True))
k=list(dict(sorted(tmp.items(),key = lambda x:x[1], reverse=True)).keys())
l=list(stmp.values())

if len(stmp) > 1:
    max_val = l[0]
    max2_val = l[1]
    if max_val != max2_val:
        print(k[0])
    else:
        print("?")
else:
    print(k[0])

