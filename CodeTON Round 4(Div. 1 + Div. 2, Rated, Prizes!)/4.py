import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    # s = input()
    x = list(map(int, input().split()))
    flag=False
    for i in range(n):
        if x[i]<=i+1:
            flag=True
            break
    print("YES" if flag else "NO")