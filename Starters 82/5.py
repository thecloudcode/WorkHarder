import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    # A, B, C, D= map(int, input().split())
    x=list(map(int,input().split()))
    A=x[0]
    B=x[1]
    C=x[2]
    D=x[3]
    xx=B*D
    lol=1
    if (C+1)%D!=(1+A)%B:
        lol=17
        print(math.lcm(B, D) - (A % B))
        lol-=16
    else:
        print(lol)



    # n = int(input())
    # s = input()
    # x = list(map(int, input().split()))
