import math
from collections import defaultdict
#
for _ in range(int(input())):
    # d=defaultdict(lambda:0)
    # a, b,c = map(int, input().split())
    # print("+" if a+b==c else "-")
    n = int(input())
    # s = input()
    x = sorted(list(map(int, input().split())))
    summ=1
    flag=True
    if x[0] != 1:
        flag = False
    if flag:
        for i in range(1,n):
            if x[i]>summ:
                flag = False
                break
            elif x[i]<=summ:
                summ+=x[i]
                continue

    print("YES" if flag else "NO")