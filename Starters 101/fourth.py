# import collections
# from collections import defaultdict
# import math
# d=defaultdict(lambda:0)
# for _ in range(int(input())):
#     # n=int(input())
#     a,b=map(int,input().split())
#     x=list(map(int,input().split()))
#
#     h=max(x)
#     l=0
#     while(l<h):
#         cal=0
#         mid=(l+h)//2
#         # for i in x:
#         #     cal+=max(0,i-mid)
#         cal=sum(max(0,i-mid) for i in x)
#         if cal<=b:
#             high=mid
#         else:
#             l=mid+1
#     print(l)