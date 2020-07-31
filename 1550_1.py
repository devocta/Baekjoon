n = list(input())
n.reverse()
res = 0
nd = {"A" : 10, "B" : 11, "C": 12, "D" : 13, "E": 14, "F" :15}
pv = 0
pvn = (1, 16, 256, 4096, 65536, 1048576)
nl = list(nd.keys())

for num in n:
    if num in nl:
        res += nd.get(num) * pvn[pv]
        pv +=1
    else:
        res += int(num) * pvn[pv]
        pv +=1
print(res)