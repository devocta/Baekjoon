h,m=map(int,input().split())
a=int(input())
t=m+a
while t>= 60:
    t-=60
    if h==23:
        h=0
    else:
        h+=1
print(h,t)