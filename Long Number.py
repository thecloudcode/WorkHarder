import collections
from collections import defaultdict
d=defaultdict(lambda:0)

l=int(input())
n=list(input())
x=list(map(str,input().split()))

ind=1
for i in x:
    d[str(ind)]=i
    ind+=1

ind=0
for i in range(l):
    if d[n[i]]>n[i]:
        break
    print(n[i],end="")
    ind+=1
flag=True
for i in range(ind,l):
    if d[n[i]]>=n[i] and flag:
        print(d[n[i]],end="")
    else:
        flag=False
        print(n[i],end="")