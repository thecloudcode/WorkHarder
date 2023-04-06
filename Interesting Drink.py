from collections import defaultdict
n=int(input())
d=defaultdict(lambda: 0)
x=sorted(list(map(int,input().split())))
for i in range(n):
    d[x[i]]=i+1
d[-1]=0
for i in range(100001):
    if d[i]==0:
        d[i]=d[i-1]
q=int(input())
for i in range(q):
    xx=int(input())
    print(d[xx])



# def search(x,s):
#     l=0
#     r=len(x)-1
#     mid=(l+r)//2
#     while(l<=r):
#         mid=(l+r)//2
#         if x[mid]==s:
#             r=mid
#             break
#         elif x[mid]>s:
#             r=mid-1
#         else:
#             l=mid+1
#     # if s in x:
#     #     count=x.count(s)
#     #     if count>1:
#     #         return r+count
#     return r+1
#     # if id!=len(x)-1 and s>x[mid+1]:
#     #     return mid+1
#     # elif mid!=0 and s<x[mid-1]:
#     #     return mid-1
#     # else:
#     #     return mid
#
# n=int(input())
# x=sorted(list(map(int,input().split())))
# nn=int(input())
# for i in range(nn):
#     xx=int(input())
#     # if xx not in x:
#     print(search(x,xx))
#     # else:
#         # print(n-x[::-1].index(xx))
