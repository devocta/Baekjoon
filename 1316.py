c,cnt=0,0
t=[0 for i in range(26)]
for _ in range(int(input())):
    st=list(input())
    prv=0
    for s in st:     
        if t[ord(s)-97] == 0:
            t[ord(s)-97] +=1
            prv=s
            c+=1
        elif s == prv:
            t[ord(s)-97] +=1
            c+=1
        else:
            c=0
            break
    
    t=[0 for i in range(26)]
    if c>0:
        cnt+=1
    c=0
print(cnt)

