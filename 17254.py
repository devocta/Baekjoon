n,m=map(int,input().split())
l=[]
for _ in range(int(m)):
    a,b,c=input().split()
    l.append([int(a),int(b),c])
l.sort(key=lambda x: [x[1], x[0]])
s=[]
for i in l:
   s.append(i[2])
print("".join(s))

