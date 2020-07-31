n,m=map(int,input().split())
*a,=map(int,input().split())
MAX=0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            tmp = a[i]+a[j]+a[k]
            if tmp <= m and tmp > MAX:
                MAX=tmp
print(MAX)
                
