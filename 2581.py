def p(n):
    num= set(range(2, n+1))
    for i in range(2, n+1):
    	if i in num:
        	num -= set(range(2*i, n+1, i))
    return list(num)
et=p(10000)
et.sort()

M=int(input())
N=int(input())
res=[]

for i in et:
    if M<=i<=N:
        res.append(i)
    elif i>N:
        break
if len(res)==0:
    print(-1)
else:
    print(sum(res))
    print(min(res))
