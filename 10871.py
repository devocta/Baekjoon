a,x=map(int,input().split())
l=list(input().split(" "))
for i in range(len(l)):
    if int(l[i]) < x:
        print(l[i], end=" ")
