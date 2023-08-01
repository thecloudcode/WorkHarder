from collections import defaultdict
import math

for _ in range(int(input())):
    # n=int(input())
    # x=list(map(int,input().split()))
    a,b=map(int,input().split())
    # s=input()
    # d=defaultdict(lambda:0)

    if b>a:
        print("NO")
    elif b==a:
        print("YES")
    else:
        x=[a].copy()[0]
        while(x%2==0):
            x//=2

        print("YES" if b%x==0 else "NO")