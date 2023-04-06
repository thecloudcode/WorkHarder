for _ in range(int(input()))
    f=0
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=int(input())
    r=list(map(int,input().split()))
    i=0
    while(i<n):
        if b[i]>a[i]:
            f=-1
            break
        elif 