from collections import defaultdict
d=defaultdict(lambda:[[],0])

n=int(input())
for i in range(1,n+1):
    a,b=map(int,input().split())
    d[a][1]+=1
    d[b]+=1

for i in range(1,n+1):
