for _ in range(int(input())):
    n,q=map(int,input().split())
    x=sorted(list(map(int,input().split())))[::-1]
    sumx=[]
    sumlol=0
    for i in x:
        sumlol+=i
        sumx.append(sumlol)
    # print(sumx)
    for __ in range(q):
        z=int(input())
        if z>sumx[-1]:
            print(-1)
            continue
        l=1
        r=n
        ans=0
        while(l<=r):
            mid=(l+r)//2
            if sumx[mid-1]>=z:
                ans=mid
                r=mid-1
            else:
                l=mid+1
        print(ans)
