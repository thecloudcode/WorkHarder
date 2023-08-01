for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))

    if len(x)==3:
        a=min(x)
        b=max(x)
        c=sum(x)-a-b

        d=min(y)
        e=max(y)
        z=d-a
        if e-b==z:
            print(z)
        else:
            print(e-c)
        continue

    if len(x)==2:
        a=min(x)
        b=max(x)
        c=y[0]

        if c-b>0:
            print(c-b)
        else:
            print(c-a)
        continue

    maxx=x[0]
    minx=min(x[0],x[1])
    minxx=max(x[0],x[1])
    for i in x:
        if i<minx:
            minxx=minx
            minx=i
        if i>maxx:
            maxx=i
    # print(maxx,minx,minxx)

    maxy = y[0]
    miny = min(y[0], y[1])
    minyy = max(y[0], y[1])
    for i in y:
        if i < miny:
            minyy = miny
            miny = i
        if i > maxy:
            maxy = i
    # print(maxy, miny, minyy)

    a=miny-minx
    if maxy-maxx==a:
        print(a)
    else:
        print(minyy-minxx)