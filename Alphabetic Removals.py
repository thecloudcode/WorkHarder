from collections import defaultdict
d=defaultdict(lambda:0)
dd=defaultdict(lambda:0)

n,k=map(int,input().split())
s=input()
for i in s:
    d[i]+=1

for i in "abcdefghijklmnopqrstuvwxyz":
    if k==0:
        break
    if d[i]>0:
        if d[i]<=k:
            dd[i]=d[i]
            d[i]=0
            k-=dd[i]
        else:
            dd[i]=k
            d[i]-=k
            k=0
# print(dict(d))
# print(dict(dd))
for i in s:
    if dd[i]>0:
        dd[i]-=1
    else:
        print(i,end="")

# ind=ord('a')
# while(k):
#     while(d[chr(ind)]==0):
#         ind+=1
#     d[chr(ind)]-=1
#     k-=1
# ans=""
#
# for i in s[::-1]:
#     if(d[i]>0):
#         ans=i+ans
#         d[i]-=1
# print(ans)