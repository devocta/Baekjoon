import sys

n = int(sys.stdin.readline())
while n:
    a, b = map(int, sys.stdin.readline().strip().split())
    print(a+b)
    n -=1
