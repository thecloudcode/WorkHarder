from collections import *
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    d=defaultdict(int)
    c=0
    x=0
    for i in range(n):
        if sum(a[:i+1:])<=m:
            c=len(a[:i+1:])
            x=i
            # print(1,x)
    if c==1:
        if a[x+1]<=m:
            x=[a[x+1]]
            # print(2,x)

        else:
            x=[a[x]]
            # print(3,x)
    elif x==0:
        x=[]
    else:
        x=a[:x+1:]
    y=[]
    for i in range(n):
        if a[i] in x:
            y.append(i+1)
            x.remove(a[i])
        # print(4,x)
    aa=a.copy()
    # a=list(set(a))
    for i in range(len(a)):
        if i+1 in y:
            d[i+1]+=len(a[:a.index(a[i]):])
        else:
            d[i+1]+=len(a[:a.index(a[i]):])+1
    # for i in range(n):

    d[-1]=0 if x==0 else len(x)
    print(d)
    post=1
    for i,j in d.items():
        if j>d[-1]:
            post+=aa.count(i)
    print(post)
