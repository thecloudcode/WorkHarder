import math
from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(lambda:0)
    dd = defaultdict(lambda:0)
    ddd = defaultdict(lambda:0)
    # x,y = map(int, input().split())
    n = int(input())
    x=list(map(int,input().split()))

    c=0
    maxx=x[0]
    dd[maxx]=maxx
    for i in x[1::]:
        if i>maxx:
            maxx=i
            dd[i]=maxx
        else:
            dd[i]=maxx

    xx=x[-1]
    ddd[xx]=xx
    for i in x[:-1:][::-1]:
        if i<=xx:
            xx=i
            ddd[i]=i
        else:
            ddd[i]=xx

    for i in x:
        if ddd[i]<i or dd[i]>i:
            c+=1
    # print(c)

    #
    #
    # for i in x:
    #     if d[i]==i and dd[i]!=-1:
    #         if dd[xx]==-1:
    #             dd[i]=-1
    #             c+=1



    # go=x[0]
    # for i in range(1,n):
    #     if x[i]>=go:
    #         go=x[i]
    #     else:
    #         d[go]=1
    #         d[x[i]]=1
    #         c+=1
    if c==0:
        print(((2**(len(x)))-1)%998244353)
    else:
        cc=n-c
        print((2**cc)%998244353)
