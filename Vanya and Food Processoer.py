import math

n,h,k=map(int,input().split())

x=list(map(int,input().split()))

sec=0
s=0
ind=0
while(1):
    if ind>=n:
        break
    while(ind<n and s+x[ind]<=h):
        s+=x[ind]
        ind+=1
    sec+=s//k
    s=s%k

    if ind<n and s+x[ind]>h and s<k:
        sec+=1
        s=0

    if ind>=n and s>0:
        sec+=math.ceil(s/k)
    # print(x[ind])

print(sec)