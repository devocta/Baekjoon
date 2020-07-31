input()
*a,=map(int,input().split())
cnt=0
c=0
for n in a:
    if n==1:
        continue
    elif n==2:
        cnt+=1
    else:
        for t in range(2, n):
            if n%t==0:
                c=0
                break
            else:
                c+=1
        if c>0:
            cnt+=1
            c=0
        else:
            c=0
print(cnt)
        
                

        
        