from math import sqrt
from collections import defaultdict

for _ in range(int(input())):

    n=int(input())
    x=list(map(int,input().split()))

    d = defaultdict(lambda: 0)

    for i in x:
        t=i`
        for j in range(2,int(sqrt(i))+1):
            while(t%j==0):
                d[j]+=1
                t//=j
        if t!=1:
            d[t]+=1
    c=1
    for i,j in d.items():
        c*=j+1
    print(c)




