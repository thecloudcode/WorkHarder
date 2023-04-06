for _ in range(int(input())):
    n,x =map(int,input().split())
    l=list(map(int,input().split()))
    if (sum(l)>=(n*x)):
        print(0)
    else:
        print(abs(sum(l)-(n*x)))