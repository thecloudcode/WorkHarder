from collections import defaultdict
for _ in range(int(input())):
    d = defaultdict(lambda: 0)
    n=int(input())
    x=sorted(list(map(int,input().split())))[::-1]
    ind=0
    pairs=0
    for i in range(n-1):
        if d[i]==1:
            continue
        for j in range(i+1,n):
            if d[i]==1 or d[j]==1:
                continue
            if x[i]>=2*x[j]:
                pairs+=1
                d[i]=1
                d[j]=1
    print(pairs,n-2*pairs)

