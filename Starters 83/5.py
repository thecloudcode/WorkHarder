import math
from collections import defaultdict

for _ in range(int(input())):
    # d = defaultdict(lambda:0)
    # a,b = map(int, input().split())
    n = int(input())
    # s = input()
    x = sorted(list(map(int, input().split())))
    if n<3:
        print("NO")
    else:
        z = x.count(max(x))
        if z==1:
            if x[0]<x[-2]:
                print("YES")
            else:
                print("NO")
        else:
            if n%2==1:

                if z<=(n//2)+1:
                    print("YES")
                else:
                    print("NO")
            else:
                if z<=n//2:
                    print("YES")
                else:
                    print("NO")

