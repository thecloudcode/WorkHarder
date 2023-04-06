import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    a,b = map(int, input().split())
    # n = int(input())
    # s = input()
    # x = list(map(int, input().split()))
    if a*5>=b:
        print("YES")
    else:
        print("NO")
