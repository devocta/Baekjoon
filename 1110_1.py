n=int(input())
a=n
cnt=0
while a!=n or cnt==0:
    n=(n%10)*10 +((n//10)+(n%10))%10
    cnt+=1
print(cnt)