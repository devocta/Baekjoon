n=int(input())
cnt=1
while n:
    a,b=map(int,input().split())
    print("Case #{}: {}".format(cnt,a+b))
    cnt +=1
    n -=1