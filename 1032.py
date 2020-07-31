n=int(input())
t=[]
while n:
    t.append(input())
    n-=1
std=t[0]
cnt=0
del t[0]
tmp=len(std)
for s in t:
    for c in range(len(std)):
        if std[c]==s[c]:
            cnt+=1
        else:
            if cnt <= tmp:
                tmp = cnt
                cnt=0
                break
tmp2=std[0:tmp]
while len(tmp2) != len(std):
    tmp2 +="?"
print(tmp2)