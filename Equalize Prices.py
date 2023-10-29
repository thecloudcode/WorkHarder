import math
for _ in range(int(input())):
    n,k = map(int,input().split())
    x= list(map(int,input().split()))

    s=0
    maxx = x[0]
    minn = x[0]
    for i in x:
        # s+=i
        if i>maxx:
            maxx= i
        if i<minn:
            minn= i

    if minn+k>=maxx-k:
        print(minn+k)
    else:
        print(-1)
