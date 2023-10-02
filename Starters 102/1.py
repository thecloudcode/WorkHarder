for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    mx=0
    mn=(10**8)+1
    for i in range(n-1):
        l = int((x[i] + x[i + 1]) / 2)
        r = int((x[i] + x[i + 1] + 1) / 2)
        if x[i]<x[i+1]:
            mn=min(l,mn)
        if x[i]>x[i+1]:
            mx=max(r,mx)
    if mx<=mn:
        print(int(mx))
    else:
        print(-1)
