n=int(input())
for _ in range(n):
    *a,=map(int, input().split())
    del a[0]
    avg=sum(a)/len(a)
    cnt=0
    for sc in a:
        if sc > avg:
            cnt+=1
    print("%0.3f" % round(cnt/len(a)*100, 3), end="")
    print("%")