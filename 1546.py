n=int(input())
l=list(map(int, input().split()))
tmp=0
for j in [i/max(l)*100 for i in l]:
    tmp+=j
print(tmp/n)
