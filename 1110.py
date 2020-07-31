s=list(map(int,input()))
if len(s) < 2:
    s.insert(0,0)
    tmp = s[0]+s[1]
    cur=list(tmp, tmp[-1])
else:
    tmp = str(s[0]+s[1])
    cur=list(map(int,(tmp, tmp[-1])))
cnt=1
while str(s[0])+str(s[1]) != str(cur[0])+str(cur[1]):
    tmp = str(cur[0]+cur[1])
    if len(tmp) < 2:
        tmp = list(0, tmp)
        cur=list(map(int,(tmp, tmp[-1])))
        cnt+=1
    else:
        cur=list(map(int,(tmp, tmp[-1])))
        cnt+=1


