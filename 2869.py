*a,=map(int,input().split())
if (a[2]-a[1])%(a[0]-a[1]) ==0:
    print((a[2]-a[1])//(a[0]-a[1]))
else:
    print((a[2]-a[1])//(a[0]-a[1])+1)
