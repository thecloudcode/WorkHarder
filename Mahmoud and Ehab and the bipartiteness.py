import collections
from collections import defaultdict

l=defaultdict(lambda:0)
r=defaultdict(lambda:0)
left=0
right=0
n=int(input())

for _ in range(n-1):
    a,b=map(int,input().split())
    if l[a]==0 and r[a]==0:
        if left<=right:
            l[a]=1
            left+=1
        else:
            r[a]=1
            right+=1
    if l[b] == 0 and r[b] == 0:
        if left <= right:
            l[b] = 1
            left+=1
        else:
            r[b] = 1
            right+=1
total=left*right
# print(left,right, dict(l), dict(r))
print(total-n+1)



