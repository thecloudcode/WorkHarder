for _ in range(int(input())):
    n,b = map(int,input().split())
    x = list(map(int,input().split()))

    k=-1
    for i in range(n-1):
        if x[i+1]