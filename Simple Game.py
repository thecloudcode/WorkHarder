n,m=map(int,input().split())

if n==1:
    print(n)
elif n%2==1:
    mid=(n//2)+1
    if mid==m:
        print(mid-1)
    elif m<mid:
        print(m+1)
    else:
        print(m-1)
elif n%2==0:
    mid=(n//2)
    smid=mid+1
    if m==mid:
        print(smid)
    elif m==smid:
        print(mid)
    else:
        if m<mid:
            print(m+1)
        else:
            print(m-1)
