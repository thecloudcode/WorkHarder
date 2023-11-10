for _ in range(int(input())):
    n=int(input())
    maxx=0
    for __ in range(n):
        a,b=map(int,input().split())
        if maxx == 0:
            maxx = a + (b-1)//2
        else:
            maxx=min(maxx,a + (b-1)//2)

    print(maxx)
