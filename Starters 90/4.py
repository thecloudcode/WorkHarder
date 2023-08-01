from collections import defaultdict
import math
Combination
for _ in range(int(input())):
    n=int(input())
    x=sorted(list(map(int,input().split())))
    ans=0
    # a,b=map(int,input().split())
    # s=input()
    d=defaultdict(lambda:0)
    dd=defaultdict(lambda:0)
    for i in range(n):
        d[x[i]]+=1
        if x[i]<=i+1:
            ans+=math.pow(2,i+2)
            dd[x[i]]=1
    for i,j in d.items():
        if j>1 and dd[i]==1:
            ans+=j-1
    print(int(ans))
