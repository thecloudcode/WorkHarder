from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(lambda: 0)

    n,s,k=map(int,input().split())
    a=list(map(int,input().split()))

    for i in a:
        d[i]=1
    sl=[s].copy()[0]
    sr=[s].copy()[0]
    # print(sl,sr)
    while(sl>0):
        if d[sl]==0:
            break
        sl-=1
    while (sr <=n):
        if d[sr] == 0:
            break
        sr += 1
    ans=[]
    if d[sl]==0 and sl!=0:
        ans.append(abs(s-sl))
    if d[sr]==0 and sr<=n:
        ans.append(abs(sr-s))
    print(min(ans))
    #
    # print(dict(d))

    # print(sl,sr)

    # print(min(abs(s-sl),abs(s-sr)))
