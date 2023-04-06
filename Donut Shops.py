for _ in range(int(input())):
    a,b,c=map(int,input().split())
    x=c/b
    if a>x:
        print(-1,b)
    elif a==x:
        print(1,-1)
    else:
        print(1,b)