for _ in range(int(input())):
    n,s=map(int,input().split())
    x=list(map(int,input().split()))

    xx=0
    c=0
    maxx=0
    f=True
    for i in range(n):
        if x[i]>maxx and f:
            maxx=x[i]
            c=i+1
        if xx+x[i]<=s:
            xx+=x[i]
        elif f:
            xx-=maxx
            f=False
        else:
            break
    print(c if f==False else 0)
