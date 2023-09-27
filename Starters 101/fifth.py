import collections
from collections import defaultdict
import math
d=defaultdict(lambda:0)


for _ in range(int(input())):
    # n=int(input())
    a,b=map(int,input().split())
    # x=list(map(int,input().split()))
    x=input()
    xx=input()

    i=0
    ans=10*b
    while(i<=a-b):
        lol=0
        ii=0
        while(ii<b):
            lol+=min(abs(int(x[i+ii])-int(xx[ii])), 10-abs(int(x[ii+i])-int(xx[ii])))
            ii+=1
        ans=min(ans,lol)
        i+=1
    print(ans)