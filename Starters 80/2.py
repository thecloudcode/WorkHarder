from collections import defaultdict
for _ in range(int(input())):
    d = defaultdict(lambda: 0)
    n=int(input())
    a=list(map(int,input().split()))
    maxx=0
    for i in a:
        d[i]+=1
        if(maxx<d[i]):
            maxx=d[i]
    print(n-maxx)