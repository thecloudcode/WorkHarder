from collections import defaultdict
for _ in range(int(input())):
    n,q=map(int,input().split())
    d=defaultdict(list)
    for i in range(n-1):
        x,y=map(int,input().split())
        d[x].append(y)

