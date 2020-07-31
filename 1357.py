x,y=map(list,input().split())
x,y=x[::-1], y[::-1]
tmp = [int(x)+int(y) for x,y in zip(x, y)]

if len(tmp) == 1:
    if str(tmp[0])[1] == "0":
        tmp = str(tmp[0])[0]
    else:
        tmp = str(tmp[0])[0] +str(tmp[0])[1]
tmp = list(map(str, tmp))
print("".join(tmp[::-1]))

