from collections import defaultdict
for _ in range(int(input())):
    d = defaultdict(lambda: 0)

    maxx=-1
    m,n=map(int,input().split())
    x=list(map(int,input().split()))
    if 2*n<m:
        print(f"Case #{_+1}: NO")
    else:
        for i in x:
            d[i]+=1
            maxx=max(maxx,d[i])
        if maxx>2:
            print(f"Case #{_+1}: NO")
        else:
            print(f"Case #{_+1}: YES")