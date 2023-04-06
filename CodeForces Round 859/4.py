import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    a, b = map(int, input().split())
    x = list(map(int, input().split()))
    prev=[x[0]]
    summ=sum(x)
    for i in x[1::]:
        prev.append(prev[-1]+i)
    for i in range(b):
        l, r,k = map(int, input().split())
        lol=summ-prev[r-1]-(prev[l-1]-x[l-1])+k*(r-l+1)
        # print(prev[-1],prev[r]-prev[l-1],k*(r-l+1))
        if lol%2==1:
            print("YES")
        else:
            print("NO")

    # n = int(input())
    # s = input()
