n=int(input())
nl=[]
for _ in range(n):
    t=int(input())
    if t!=0:
        nl.append(t)
    else:
        del nl[-1]
if len(nl)==0:
    print(0)
else:
    print(sum(nl))
