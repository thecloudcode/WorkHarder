import math
from collections import defaultdict


for _ in range(int(input())):
    d = defaultdict(lambda: 0)

    # n = int(input())
    # x = list(map(int, input().split()))
    n,k= map(int, input().split())
    s=input()
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    q=int(input())
    x = list(map(int, input().split()))
    ind=0
    i=0
    # for i in range(k):
    while(1):
        if ind>=q or i>=n:
            break
        if l[i]>x[ind]:
            while(ind<q):
                if l[i]<=x[ind]:
                    break
                ind+=1
        if r[i]<x[ind]:
            i+=1
            continue
        a=min(x[ind],r[i]+l[i]-x[ind])
        b=max(x[ind],r[i]+l[i]-x[ind])
        if a<b:
            d[a-1]=b-1
        i+=1
    print(dict(d))
    i=0
    while(i<n):
        if d[i]!=0:
            j=d[i]
            while(j>=i):
            # for j in range(i,d[i]+1):
                print(s[j],end="")
                j-=1
            i=d[i]+1
        else:
            print(s[i],end="")
            i+=1
    print()
