n,k=map(int,input().split())
res=1
for _ in range(k):
    res*=n
    n-=1
f=1
for k in range(1,k+1):
   f*= k
print(res//f) 
