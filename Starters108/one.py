import math
from collections import defaultdict

for _ in range(int(input())):
    d = defaultdict(lambda: 0)
    ind = defaultdict(lambda: -1)

    n=int(input())
    x=list(map(int,input().split()))
    x.append(-1)
    # a,b,c=map(int,input().split())
    # s=input()

    for i in range(n):
        if ind[x[i]]==-1:
            ind[x[i]]=i
        else:
            d[x[i]]=max(d[x[i]],i-ind[x[i]])
            ind[x[i]]=i
        if x[i]==-1:
            for ii in list(set(x)):
                d[ii] = max(d[ii], n-1-ind[ii])
            break
    maxx=n
    ans=-1
    for i,j in d.items():
        if j<maxx:
            maxx = j
            ans = i
    print(i,math.ceil(maxx/2))
    
