import math
from collections import defaultdict
#
for _ in range(int(input())):
    d=defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    # s = input()
    # x = list(map(int, input().split()))
    x=[]
    lol=[]
    xx=1
    for i in range(n*n):
        if xx>n*n:
            xx=2
        lol.append(str(xx))
        if len(lol)==n:
            x.append(lol)
            lol=[]
        xx+=2
    for i in x:
        print(' '.join(i))


