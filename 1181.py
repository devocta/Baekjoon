n=int(input())
s=dict()
for _ in range(n):
    t=input()
    if t not in s:
        s[t]=len(t)
s=dict(sorted(dict(sorted(s.items())).items(), key=lambda x: x[1])).keys()
for i in s:
    print(i)

