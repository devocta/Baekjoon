def p(n):
    num= set(range(2, n+1))
    for i in range(2, n+1):
    	if i in num:
        	num -= set(range(2*i, n+1, i))           
    return list(num)
et=p(1000000)

M,N=map(int,input().split())
res=[]
for i in et:
    if M<=i<=N:
        res.append(i)
    elif i>N:
        break
print("\n".join(map(str, res)))