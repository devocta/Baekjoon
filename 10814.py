l=[]
for _ in range(int(input())):
    a,n=input().split()
    l.append([int(a), n])
l.sort(key=lambda x: x[0])
for a,n in l:
    print(a, n)
