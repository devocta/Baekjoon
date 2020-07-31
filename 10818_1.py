n=int(input())
l=list(map(int,input().split(" ")))
MAX, MIN = 1, 1000000
for i in range(n):
    if l[i] > MAX:
        MAX = l[i]
for i in range(n):
    if l[i] < MIN:
        MIN = l[i]
print(MIN, MAX)