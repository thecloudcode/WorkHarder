import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a,b = map(int, input().split())
    # n = int(input())
    s = input()
    # x = list(map(int, input().split()))
    c=[]
    d=[]
    for i in list(s):
        if i not in d:
            c.append(list(s).count(i))
            d.append(i)
    if 4 in c:
        print(-1)
    elif 3 in c:
        print(6)
    else:
        print(4)