from collections import defaultdict
n,k=map(int,input().split())
x=list(map(int,input().split()))

hash=defaultdict(lambda:0)
for i in range(n):
    hash[x[i]]+=1

c=0
while(True):
    for i in range(1,k+1):
        if hash[i]>0 and i<k:
            hash[i+1]+=1
            hash[i]-=1
    c+=1
    print(hash)
    if hash[k]==n:
        break
print(c)
# c=0
# # ii=0
# while(1):
#     prev = x[0]
#     # ii+=1
#
#     for i in range(n):
#         if i==0:
#             x[0]+=1
#         else:
#             if x[i]==prev:
#                 continue
#             elif x[i]!=k:
#                 prev=x[i]
#                 x[i]+=1
#     c+=1
#     x.sort()
#     if (x[0] == k) and (len(list(set(x))) == 1):
#         break
#     # print(x)
# print(c)
