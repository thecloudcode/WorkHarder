for _ in range(int(input())):
    a,b,n = map(int,input().split())
    x=list(map(int,input().split()))
    s=b
    for i in x:
        s+=min(i,a-1)
    print(s)