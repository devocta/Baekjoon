a,b,n=map(int,input().split())
while n:
    a%=b
    a*=10
    res=a//b
    n-=1
print(res)