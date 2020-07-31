h,m,s=map(int,input().split())
a=int(input)
if a>=60:
    ma,sa=a//60,a%60
    print(h, ma, )
else:
    print(h, m , s+a)
if ma>=60:
    ha,ma=ma//60,m%60
else:
    print(h, m+ma, sa)
 
    