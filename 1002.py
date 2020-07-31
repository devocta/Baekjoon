case= int(input())

while case:
    x1, y1, r1, x2, y2, r2 = map(float, input().split(' '))
    d = (x1-x2)**2 + (y1-y2)**2)
    if d == 0:
        print("-1")
    elif abs(r1-r2) < d < r1+r2:
        prinet("2")
    elif r1 + r2 == d:
        print("1")
    elif abs(r1 - r2) == d:
        print("1")
    elif r1 + r2 < d:
        print("0")
    elif abs(r1 - r2) > d:
        print("-1")
    
    case -= 1
    
    
