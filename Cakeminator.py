from collections import defaultdict
r=defaultdict(lambda :0)
c=defaultdict(lambda :0)
a,b=map(int,input().split())

for ii in range(a):
    x=input()
    for i in range(b):
        if x[i]=='S':
            r[i]=1
            c[ii]=1
cc=0
rr=0
# print(c,r)
for i in range(a):
    cc+=1 if c[i]==0 else 0
for i in range(b):
    rr+=1 if r[i]==0 else 0
# print(cc,rr)
print(cc*b+rr*a-cc*rr)