for _ in range(int(input())):
    # print(_,end=" ")
    n,x=map(int,input().split())
    if n%x!=0:
        print(-1)
    else:
        for i in range(n):
            if i+1==n:
                print(1)
            elif i+1==1:
                print(x,end=" ")
            elif i+1==x:
                print(n,end=" ")
            else:
                print(i+1,end=" ")