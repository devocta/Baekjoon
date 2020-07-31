n=list(input())
def mul(lt):
    tmp=1
    for i in range(len(lt)):
        tmp*=int(lt[i])
    return tmp
if len(n)==1 and n[0]=="1":
    print("NO")
else:
    cnt=0
    for i in range(len(n)):
        tmp1=mul(n[:i+1])
        tmp2=mul(n[i+1:])
        if tmp1 == tmp2:
            cnt+=1

    if cnt >=1:
        print("YES")
    else:
        print("NO")

