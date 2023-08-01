from collections import  defaultdict
import math

for _ in range(int(input())):
    # n=int(input())
    # x=list(map(int,input().split()))
    n,k=map(int,input().split())

    o=(n+ 1) // 2

    if n < 2 * k:
        print("NO")
    elif k > o:
        print("NO")
    elif k == o:
        print("YES")
    elif (o - k) % 2 == 0:
        print("YES")
    else:
        print("NO")
    # s=input()
    # d=defaultdict(lambda:0)