for _ in range(int(input())):
    z,zz,c=map(int,input().split())
    p=list(map(int,input().split()))
    a=list(map(int,input().split()))

    maxx=0
    maxxx=z+zz
    for i in a:
        for j in p[p.index(i)+1::]:
            if(j-i+c>=maxx):
                maxx=j-i+c
                x=j
                xx=i
                print(x, xx, maxx)
                if (maxxx > p.index(x) - p.index(xx)):
                    maxxx = p.index(x) - p.index(xx)
    print(maxxx)

    # x=min(a)
    # xx=max(a)+c


