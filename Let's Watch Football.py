for _ in range(int(input().split()))
    a,b,c=map(int,input().split())
    x=list(map(int,input().split()))
    for i in range(len(x)):
        if x[i]<b:
            continue
        if x[i]>=b and x[i]-x[i-1]!=1:
            print(i-b)