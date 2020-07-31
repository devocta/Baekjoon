s=list(input())
n= [-1 for i in range(ord("z")-ord("a")+1)]
for i in range(len(s)):
    if n[ord(s[i])-97] == -1:
        n[ord(s[i])-97] = i
print(" ".join(map(str, n)))
