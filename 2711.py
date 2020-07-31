n=int(input())
while n:
    i,s=input().split()
    tmp=list(s)
    del tmp[int(i)-1]
    print("".join(tmp))
    n-=1