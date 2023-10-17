from collections import defaultdict
d=defaultdict(lambda: 0)

n,m,k = map(int,input().split())
x=list(map(int,input().split()))
xx=[]


for i in range(m):
    xx.append(list(map(int,input().split())))

for _ in range(k):
    a,b=map(int,input().split())
    a-=1
    b-=1
    for i in range(a,b+1):
        d[i]+=1

# print(d)
for i,j in d.items():
    s=xx[i][0]-1
    e=xx[i][1]-1
    d=(xx[i][2])*j

    for xxx in range(s,e+1):
        x[xxx]+=d

for i in range(n):
    if i==n-1:
        print(x[i])
    else:
        print(x[i], end=" ")