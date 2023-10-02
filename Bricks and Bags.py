from bisect import bisect_right
# print(bisect_right([1],1))
for _ in range(int(input())):
    n=int(input())
    x=sorted(list(map(int,input().split())))
    one=x[0]
    onei=bisect_right(x,one)-1

    last=x[-1]
    lasti=x.index(last)

    # minn=abs(x[0]-x[1])+abs(x[1]-x[2])
    minnflag=False
    minn=0
    for i in x[onei+1:lasti:]:
        xx=abs(one-last)+abs(last-i)
        if minnflag:
            minn=min(minn,xx)
        else:
            minn=xx
    print(minn)

