import collections
from collections import defaultdict

d=defaultdict(lambda:0)
s=defaultdict(lambda:0)
e=defaultdict(lambda:0)


n=int(input())
x=list(map(int,input().split()))

for i in range(n):
    d[x[i]]+=1
    if d[x[i]]==1:
        s[x[i]]=i
        e[x[i]]=i
    else:
        e[x[i]]=i

mval=-1
mdis=0
one=0
two=0
for i,j in d.items():
    # print(i,j)
    if j>mval:
        mval=j
        mdis=e[i]-s[i]+1
        one=s[i]
        two=e[i]
    elif mval==j and e[i]-s[i]+1<mdis:
        # mval = j
        mdis = e[i] - s[i] + 1
        one = s[i]
        two = e[i]
print(one+1, two+1)