for _ in range(int(input())):
    # n=int(input())
    x=list(map(int,input().split()))
    a=max(list(map(int,input().split())))
    b=max(list(map(int,input().split())))
    print("YES" if a>b else "NO")
