import math
from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(lambda:0)
    n,k = map(int, input().split())
    # n = int(input())
    # s = input()
    x = list(map(str, input().split()))
    y = list(map(str, input().split()))
    # x=input()
    # y=input()
    #
    # xx=list(map(str,x.split()))
    # yy=list(map(str,y.split()))

    flag=True
    for i in range(n):
        if len(x[i])!=len(y[i]):
            flag=False
            break
        for j in range(len(x[i])):
            d[x[i][j]]+=1
    if flag:

        for i in y:
            for j in i:
                d[j]-=1

        z=list(d.values())
        if max(max(z),abs(min(z)))<=k:
            print("YES")
        else:
            print("NO")
        # print(xx,yy)
    else:
        print("NO")