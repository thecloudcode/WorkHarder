from collections import defaultdict
for _ in range(int(input())):
    d = defaultdict(lambda: 0)
    n,m=map(int,input().split())
    x=[]
    r=0
    c=0
    ci=0
    ri=0
    for __ in range(n):
        s=input()
        x.append(s)
        rr=0
        for i in range(m):
            if s[i]=='*':
                d[i]+=1
                rr+=1
        if rr>r:
            r=rr
            ri=__
    # print(dict(d),r,ri)
    for i in range(m):
        if d[i]>c:
            c=d[i]
            ci=i
    if x[ri][ci]=='*':
        print(m-r+n-c)
    else:
        print(m-r+n-c-1)
