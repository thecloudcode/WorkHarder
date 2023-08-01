import math
from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    # a = int(input())
    xxx = 0
    s = 0

    x = list(map(int,input().split()))
    for i in x:
        d[i]+=1
    if len(list(d.keys()))!=n:
        for i in range(n-1):
            d[x[i]]-=1
            s+=1
            xxx+=n-d[x[i]]-s
        print(xxx)
    else:
        print(int(n*(n-1)/2))
