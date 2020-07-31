n=int(input())
std=input()
while n-1:
    tmp=input()
    for i in range(len(std)):
        if std[i] != tmp[i]:
            std = std[:i]+"?"+std[i+1:]
    n-=1
print(std)
