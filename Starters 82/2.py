import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    # s = input()
    x = list(map(int, input().split()))
    c=0
    xx=min(x)
    for i in x:
        if i!=xx:
            c+=1
    print(c)