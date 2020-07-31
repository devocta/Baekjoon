n=int(input())
for i in range(n*2):
    if(i%2!=0):
        for j in range(n):
            if(j%2!=0):
                print("*", end="")
            else:
                print(" ", end="")
    else:
        for k in range(n):
            if(k%2!=0):
                print(" ", end="")
            else:
                print("*", end="")
    print("")