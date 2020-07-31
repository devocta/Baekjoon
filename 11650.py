n=int(input())
t=[]
for _ in range(n):
    x,y=map(int,input().split())
    t.append([x,y])
t.sort(key=lambda x: [x[0], x[1]])
for x,y in t:
    print(x, y)