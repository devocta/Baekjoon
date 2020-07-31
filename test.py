a=int(input())
s=list(input())
for i in range(a-1):
    x=input()
    for j in range(len(s)):
        if x[j]!=s[j]:
            s[j]='?'
print(*s,sep='')