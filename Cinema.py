from collections import defaultdict
d=defaultdict(lambda:0)

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
c=list(map(int,input().split()))

for i in a:
    d[i]+=1

bmax=-1
cmax=-1
ans=-1
ind=0
for i,j in zip(b,c):
    if d[i]>bmax:
        bmax=d[i]
        cmax=d[j]
        ans=ind
    elif d[i]==bmax:
        if cmax<d[j]:
            ans=ind
    ind+=1

print(ans+1)