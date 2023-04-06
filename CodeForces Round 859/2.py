import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    # s = input()
    x = list(map(int, input().split()))
    e=0
    o=0
    for i in x:
        if i%2==0:
            e+=i
        else:
            o+=i
    if e>o:
        print("YES")
    else:
        print("NO")
