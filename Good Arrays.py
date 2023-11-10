from collections import defaultdict
for _ in range(int(input())):
    d=defaultdict(lambda:0)

    n=int(input())
    x=list(map(int,input().split()))

    maxx=0
    for i in x:
        d[i]+=1
        maxx=max(maxx,d[i])

    if maxx>n//2:
        print("NO")
    else:
        print("YES")