import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    # a, b = map(int, input().split())
    n = int(input())
    # s = input()
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    flag=True

    if 1 in y and 1 not in x:
        flag=False
    if x[0]!=y[0] or x[n-1]!=y[n-1]:
        flag=False
    if flag:

        for i in range(1,n-1):
    #             # if 1 not in x[:i:] and 1 not in x[i+1::]:
    #             #     flag=False
    #             #     break
    #
            if x[i]==1 and y[i]==0:
                flag=False
                break
    print("YES" if flag else "NO")
