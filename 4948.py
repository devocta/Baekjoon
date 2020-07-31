def p(n):
    num= set(range(2, n+1))
    for i in range(2, n+1):
    	if i in num:
        	num -= set(range(2*i, n+1, i))           
    return list(num)
et=p(123456*2)
c=1
while True:
    n=int(input())
    if n==0:
        break
    res=[]
    for i in et:
        if n<i<=n*2:
            res.append(i)
        elif i>n*2:
            break
    print(len(res))