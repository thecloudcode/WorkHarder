for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=sum(l)
    for i in range(n-1):
        # a=x[]
        if x-2*l[i]-2*l[i+1]>x:
            x=x-2*l[i]-2*l[i+1]

    print(x)