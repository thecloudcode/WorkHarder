import math
from collections import defaultdict
d=defaultdict(lambda:0)

for _ in range(int(input())):
    # n=int(input())
    a,b=map(int,input().split())
    x=list(map(int,input().split()))
    print("YES" if b in x else "NO")
