n= 5
res = 0
while n:
    tmp = int(input())
    n -= 1
    if tmp > 40:
       res += tmp
    else:
        res += 40
print(res//5)
