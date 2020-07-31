str=list(input().upper())
cnt=[0 for i in range(ord("Z")-ord("A")+1)]
for s in str:
    cnt[ord(s)-65] +=1
tmp=cnt[:]
tmp.sort(reverse=True)
if len(str) > 1:
    if tmp[0] != tmp[1]:
        print(chr(cnt.index(max(cnt))+65))
    else:
        print("?")
else:
    print(chr(cnt.index(max(cnt))+65))