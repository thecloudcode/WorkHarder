import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    x = input()
    e=[]
    o=[]
    for i in range(n):
        if i%2==0:
            e.append(x[i])
        else:
            o.append(x[i])
    if(len(list(set(e) & set(o))))==0:
        print("YES")
    else:
        print("NO")
    # x = list(map(int, input().split()))
