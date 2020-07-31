while True:
    n=input()
    chk=0
    if n=='0':
        break
    else:
        for i in range(len(n)//2):
            if n[i] != n[len(n)-i-1]:
                chk+=1
                break
        if chk >= 1:
            print("no")
        else:
            print("yes")