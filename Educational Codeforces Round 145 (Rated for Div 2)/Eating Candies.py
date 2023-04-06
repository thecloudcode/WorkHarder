for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))

    ans=0
    l=0
    r=n-1
    lsum=x[l]
    rsum=x[r]
    while(l<r):
        if lsum==rsum:
            ans=l+(n-r)+1
            l+=1
            lsum+=x[l]
        elif lsum<rsum:
            l+=1
            lsum+=x[l]
        elif lsum>rsum:
            r-=1
            rsum+=x[r]
    print(ans)