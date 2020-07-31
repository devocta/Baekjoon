import sys
input()
*a,=map(int,sys.stdin.readline().split())
input()
*m,=map(int,sys.stdin.readline().split())
a.sort()
def bs(l,k):
    s=0
    e=len(l)-1
    while s<=e:
        mid=(s+e)//2
        if k == l[mid]:
            return 1
        elif k > l[mid]:
            s=mid+1
        else:
            e=mid-1
    return 0
for i in m:
    print(bs(a, i))
