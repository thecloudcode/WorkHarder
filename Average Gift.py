for _ in range(int(input())):
    n,s=map(int,input().split())
    x=list(map(int,input().split()))

    if s>=min(x) and s<=max(x):
        print("YES")
    else:
        print("NO")



