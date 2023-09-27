import math
from collections import defaultdict

d = defaultdict(lambda: 0)

for _ in range(int(input())):
    n = int(input())
    # x = list(map(int, input().split()))
    # a, b = map(int, input().split())
    i=1
    for j in range(n):
        if j==n-1:
            print(i)
        else:
            print(i,end=" ")
        i+=2
