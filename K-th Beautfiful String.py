for _ in range(int(input())):
    n,k=map(int,input().split())

    bone=n-1
    btwo=n-2

    a=1
    c=1
    while(a+c<=k):
        a+=c
        c+=1
        btwo-=1

    more=k-a
    while(more):
        bone-=1
        more-=1

    for i in range(n):
        if i==btwo or i==bone:
            print('b', end="")
        else:
            print('a',end="")
    print()
